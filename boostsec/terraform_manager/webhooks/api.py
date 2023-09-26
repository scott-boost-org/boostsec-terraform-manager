"""Webhooks API."""
import hmac
import shlex
import urllib.parse
from typing import Any, Optional

import structlog
from fastapi import APIRouter, FastAPI
from github import Github, UnknownObjectException
from github.Repository import Repository
from pydantic import BaseModel
from starlette.requests import Request
from structlog.stdlib import BoundLogger

from boostsec.terraform_manager.webhooks.settings import ApiWebhooksSettings

log: BoundLogger = structlog.get_logger(__name__)

router = APIRouter()
app = FastAPI()


class SlashCommandPayload(BaseModel):
    """Model for slack slash command request payload."""

    text: str
    command: str
    channel_name: str

    @classmethod
    def from_urlstring(cls, urlstr: str) -> "SlashCommandPayload":
        """Parse from url encoded string."""
        result = {}
        print(urlstr)
        for line in urlstr.split("&"):
            try:
                name, val = line.split("=")
                result[name] = val
            except ValueError:
                pass
        return SlashCommandPayload.parse_obj(result)


def _get_repo(token: str, repo_full_name: str) -> Repository:
    client = Github(token)
    return client.get_repo(repo_full_name)


class Health(BaseModel):
    """Health status report."""

    status: str


@router.get("/_boostsecurity/readiness")
@router.get("/_boostsecurity/liveness")
@router.get("/terraform-manager-webhooks")
async def health_check() -> Health:
    """Return something."""
    return Health(status="OK")


def to_inputs(text: str) -> dict[str, Any]:
    """Convert cli string to dict."""
    result = {}
    print(text)
    unquoted = urllib.parse.unquote(text).replace("+", " ")
    print(unquoted)
    for arg in shlex.split(unquoted):
        name, value = arg.split("=")
        result[name] = value
    return result


def _build_response(
    is_ok: bool, msgs: list[str], response_type: str = "in_channel"
) -> dict[str, Any]:
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": msg,
            },
        }
        for msg in msgs
    ]
    return {
        "attachments": [{"color": "#2eb67d" if is_ok else "#e01e5a", "blocks": blocks}],
        "response_type": response_type,
    }


@router.post("/terraform-manager-webhooks/slash-command")
async def slash_command(
    request: Request,
) -> dict[str, Any]:
    """Handle slash command webhook from slack."""
    settings: ApiWebhooksSettings = app.state.settings

    request_timestamp = request.headers["X-Slack-Request-Timestamp"]
    request_body = await request.body()
    base_secret = ":".join(
        [
            "v0",
            request_timestamp,
            request_body.decode(),
        ]
    )
    computed_secret = hmac.new(
        key=settings.slack_signing_secret.encode(),
        msg=base_secret.encode(),
        digestmod="sha256",
    ).hexdigest()
    if not hmac.compare_digest(
        f"v0={computed_secret}", request.headers["X-Slack-Signature"]
    ):
        return _build_response(False, ["Failed to verify signature"], "ephemeral")

    urlstring = request_body.decode()
    command_payload = SlashCommandPayload.from_urlstring(urlstring)
    if command_payload.channel_name == "directmessage":
        return _build_response(
            False,
            ["Sorry this bot cannot be triggered inside a direct message."],
            "ephemeral",
        )
    command_text = command_payload.text
    if command_text == "help":
        return _build_response(
            True,
            [
                "```/gh-actions repo-full-path=org/repo "
                "workflow-id=myWorkflow.yml name=Scott```",
                "`repo-full-path`: Full path to the repository "
                "where the workflow is located in.",
                "`workflow-id`: Name of workflow file to be triggered.",
            ],
            "ephemeral",
        )
    try:
        inputs = to_inputs(command_text)
    except ValueError:
        return _build_response(
            False,
            [
                "All arguments must be of the form `name=value`",
            ],
            "in_channel",
        )
    try:
        repo_full_path = inputs.pop("repo-full-path")
        workflow_id = inputs.pop("workflow-id")
    except KeyError as e:
        return _build_response(
            False,
            [
                f"Missing kwarg: `{e.args[0]}`",
            ],
            "in_channel",
        )
    try:
        repo = _get_repo(settings.github_token, repo_full_path)
    except UnknownObjectException:
        return _build_response(
            False,
            [
                f"Cannot access repo: `{repo_full_path}`",
            ],
            "in_channel",
        )
    try:
        workflow = repo.get_workflow(workflow_id)
    except UnknownObjectException:
        return _build_response(
            False,
            [
                f"Cannot find workflow: `{workflow_id}`",
            ],
            "in_channel",
        )
    success = workflow.create_dispatch(
        repo.default_branch,
        inputs,
    )
    if success:
        return _build_response(
            True,
            [
                "Successfully dispatched workflow "
                f"`{workflow_id}` in repository "
                f"`{repo_full_path}` with kwargs: {inputs}",
            ],
            "in_channel",
        )
    else:
        url = (
            "https://github.com/"
            f"{repo_full_path}/blob/{repo.default_branch}/"
            f".github/workflows/{workflow_id}"
        )
        return _build_response(
            True,
            [
                "Workflow dispatch failed. "
                "Probably missing required inputs. "
                f"Please check {url}"
            ],
            "in_channel",
        )


def create_app(
    api_webhooks_settings: Optional[ApiWebhooksSettings] = None,
) -> FastAPI:
    """Configure the app."""
    app.include_router(router)

    api_webhooks_settings = api_webhooks_settings or ApiWebhooksSettings()
    app.state.settings = api_webhooks_settings

    return app


def main() -> FastAPI:  # pragma: nocover
    """Entrypoint for the application."""
    return create_app()
