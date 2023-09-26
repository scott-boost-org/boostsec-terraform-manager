"""Webhooks API."""
import hmac
import shlex
import urllib.parse
from typing import Any, Optional

import structlog
from fastapi import APIRouter, FastAPI
from github import Github
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


@router.post("/terraform-manager-webhooks/slash-command")
async def slash_command(
    request: Request,
) -> dict[str, Any]:
    """Handle slash command webhook from slack."""
    settings: ApiWebhooksSettings = app.state.settings
    response: dict[str, Any] = {"blocks": [], "response_type": "in_channel"}

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
        response["response_type"] = "ephemeral"
        response["blocks"].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Failed to verify.",
                },
            }
        )
        return response

    urlstring = request_body.decode()
    command_payload = SlashCommandPayload.from_urlstring(urlstring)
    if command_payload.channel_name == "directmessage":
        response["response_type"] = "ephemeral"
        response["blocks"].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        "Sorry this bot cannot be triggered inside a direct message."
                    ),
                },
            }
        )
        return response
    command_text = command_payload.text
    if command_text == "help":
        response["response_type"] = "ephemeral"
        response["blocks"].extend(
            [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            "```/gh-action repo-full-path=org/repo "
                            "workflow-id=myWorkflow.yml name=Scott```"
                        ),
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            "`repo-full-path`: Full path to the repository "
                            "where the workflow is located in."
                        ),
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            "`workflow-id`: Name of workflow file to be triggered."
                        ),
                    },
                },
            ]
        )
        return response
    try:
        inputs = to_inputs(command_text)
    except ValueError:
        response["blocks"].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "All arguments must be of the form name=value.",
                },
            }
        )
        return response
    try:
        repo_full_path = inputs.pop("repo-full-path")
        workflow_id = inputs.pop("workflow-id")
    except KeyError as e:
        response["blocks"].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"Missing kwarg: `{e.args[0]}`",
                },
            }
        )
        return response

    repo = _get_repo(settings.github_token, repo_full_path)
    workflow = repo.get_workflow(workflow_id)
    success = workflow.create_dispatch(
        repo.default_branch,
        inputs,
    )
    if success:
        response["blocks"].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        "Successfully dispatched workflow "
                        f"`{workflow_id}` in repository "
                        f"`{repo_full_path}` with kwargs: {inputs}"
                    ),
                },
            }
        )
    else:
        url = (
            "https://github.com/"
            f"{repo_full_path}/blob/{repo.default_branch}/"
            f".github/workflows/{workflow_id}"
        )
        response["blocks"].append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (
                        "Workflow dispatch failed. "
                        "Probably missing required inputs. "
                        f"Please check {url}"
                    ),
                },
            }
        )
    return response


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
