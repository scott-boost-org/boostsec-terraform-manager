"""Api Webhook settings."""
from pydantic import BaseSettings


class ApiWebhooksSettings(BaseSettings):
    """Settings for webhooks api."""

    github_token: str
    repo_full_name: str
    workflow_id: str
