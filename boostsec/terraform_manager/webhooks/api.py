"""Webhooks API."""
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
    for arg in shlex.split(urllib.parse.unquote(text)):
        name, value = arg.split("=")
        result[name] = value
    return result


@router.post("/terraform-manager-webhooks/slash-command")
async def slash_command(
    request: Request,
) -> str:
    """Handle slash command webhook from slack."""
    settings: ApiWebhooksSettings = app.state.settings
    repo = _get_repo(settings.github_token, settings.repo_full_name)
    workflow = repo.get_workflow(settings.workflow_id)
    urlstring = (await request.body()).decode()
    inputs = to_inputs(SlashCommandPayload.from_urlstring(urlstring).text)
    workflow.create_dispatch(
        repo.default_branch,
        inputs,
    )
    return (
        "Successfully dispatched workflow "
        f"{settings.workflow_id} in repository {settings.repo_full_name}"
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
