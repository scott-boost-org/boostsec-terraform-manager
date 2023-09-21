from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Auth0(BaseModel):
    domain: str


class AdminDashboard(BaseModel):
    callback_urls: List[str]
    allowed_logout_urls: List[str]
    allowed_web_origins: List[str]
    initiate_login_uri: str


class Branding(BaseModel):
    logo_url: str
    primary_color: str
    background_color: str


class Connections(BaseModel):
    google_social: bool = Field(..., alias='google-social')
    google_boost: bool = Field(..., alias='google-boost')


class Organization(BaseModel):
    display_name: str
    boost_org_id: str
    boost_org_features: List[str]
    branding: Branding
    connections: Optional[Connections] = None
    connection_ids: List
    conn_defaults: Optional[bool] = None


class Tfvars(BaseModel):
    context: Dict[str, Any]
    auth0: Auth0
    boostsec_client_api_audience: str
    callback_urls: List[str]
    allowed_logout_urls: List[str]
    allowed_web_origins: List[str]
    initiate_login_uri: str
    admin_dashboard: AdminDashboard
    organizations: dict[str, Organization]
