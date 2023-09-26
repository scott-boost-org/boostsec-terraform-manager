"""Api Webhook settings."""
from pydantic import BaseSettings


class ApiWebhooksSettings(BaseSettings):
    """Settings for webhooks api."""

    github_token: str
    slack_signing_secret: str
