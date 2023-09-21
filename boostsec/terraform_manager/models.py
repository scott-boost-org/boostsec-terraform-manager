"""HCL tfvars model for terraform-releases."""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class Auth0(BaseModel):
    """Auth0 configuration."""

    domain: str


class AdminDashboard(BaseModel):
    """Admin dashboard configuration."""

    callback_urls: List[str]
    allowed_logout_urls: List[str]
    allowed_web_origins: List[str]
    initiate_login_uri: str


class Branding(BaseModel):
    """Branding configuration."""

    logo_url: str = "https://boostsecurity.io/images/programmers-01-1.svg"
    primary_color: str = "#4087c8"
    background_color: str = "#ffffff"


class Organization(BaseModel):
    """Organization configuration."""

    display_name: str
    boost_org_id: str
    boost_org_features: list[str]
    branding: Branding
    connections: Optional[dict[str, bool]] = None
    connection_ids: list[str]
    conn_defaults: Optional[bool] = None


class Tfvars(BaseModel):
    """Tfvars model."""

    context: Dict[str, Any]
    auth0: Auth0
    boostsec_client_api_audience: str
    callback_urls: list[str]
    allowed_logout_urls: list[str]
    allowed_web_origins: list[str]
    initiate_login_uri: str
    admin_dashboard: AdminDashboard
    organizations: dict[str, Organization]
