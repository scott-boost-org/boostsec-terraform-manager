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


def add_feature_flag_for_orgs(
    feature_flag: str, model: Tfvars, orgs: Optional[list[str]] = None
) -> Tfvars:
    """Add feature flag to all organizations."""
    org_mapping: dict[str, Organization] = {**model.organizations}
    for org_name in org_mapping:
        if orgs and org_name not in orgs:
            continue
        org_mapping[org_name] = evolve(
            org_mapping[org_name],
            boost_org_features=[*org_mapping[org_name].boost_org_features, feature_flag]
            if feature_flag not in org_mapping[org_name].boost_org_features
            else org_mapping[org_name].boost_org_features,
        )
    return evolve(model, organizations=org_mapping)
