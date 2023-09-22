"""Organization."""
from typing import Any, Optional, TypeVar
from uuid import uuid4

from pydantic import BaseModel

from boostsec.terraform_manager.models import Branding, Organization, Tfvars

T = TypeVar("T", bound=BaseModel)


def evolve(obj: T, **overrides: Any) -> T:
    """Create a new object overriding specified field, use to evolve a frozen obj."""
    new_attributes: dict[str, Any] = {**dict(obj), **overrides}
    return obj.__class__(**new_attributes)


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


def add_feature_flag_for_all_orgs(feature_flag: str, model: Tfvars) -> Tfvars:
    """Add feature flag to all organizations."""
    orgs: dict[str, Organization] = {**model.organizations}
    for org_name in orgs:
        orgs[org_name] = evolve(
            orgs[org_name],
            boost_org_features=[*orgs[org_name].boost_org_features, feature_flag],
        )
    return evolve(model, organizations=orgs)
