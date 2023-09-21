"""HCL tfvars model for terraform-releases."""
from typing import Any, Dict, List, Optional
from uuid import uuid4

from boostsec.common.pydantic import evolve
from pydantic import BaseModel, Field


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


def add_organization(
    model: Tfvars,
    org_name: str,
    display_name: str,
    features: Optional[list[str]] = None,
    branding: Optional[Branding] = None,
    connections: Optional[dict[str, bool]] = None,
    connection_ids: Optional[list[str]] = None,
    conn_defaults: Optional[bool] = None,
) -> Tfvars:
    """Add organization."""
    return evolve(
        model,
        organizations={
            **model.organizations,
            org_name: Organization(
                display_name=display_name,
                boost_org_id=str(uuid4()),
                boost_org_features=features or [],
                branding=branding or Branding(),
                connections=connections,
                connection_ids=connection_ids or [],
                conn_defaults=conn_defaults,
            ),
        },
    )


def add_feature_flag(feature_flag: str, model: Tfvars) -> Tfvars:
    """"""
    orgs: dict[str, Organization] = {**model.organizations}
    for org_name in orgs:
        orgs[org_name] = evolve(
            orgs[org_name],
            boost_org_features=[*orgs[org_name].boost_org_features, feature_flag],
        )
    return evolve(model, organizations=orgs)
