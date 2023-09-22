"""Model Factories."""
from typing import Any

from pydantic_factories import ModelFactory, Use

from boostsec.terraform_manager.models import Organization, Tfvars


EmptyDictFactory: Use[Any, dict[Any, Any]] = Use(lambda: {})
EmptyListFactory: Use[Any, list[Any]] = Use(lambda: [])


class TfvarsFactory(ModelFactory[Tfvars]):
    """Factory for Tfvars."""

    __model__ = Tfvars

    context = EmptyDictFactory
    callback_urls = EmptyListFactory
    allowed_logout_urls = EmptyListFactory
    allowed_web_origins = EmptyListFactory
    organizations = EmptyDictFactory


class OrganizationFactory(ModelFactory[Organization]):
    """Factory for Organization."""

    __model__ = Organization

    boost_org_features = EmptyListFactory
    connections = Use(lambda: None)
    connection_ids = EmptyListFactory
    conn_defaults = Use(lambda: None)
