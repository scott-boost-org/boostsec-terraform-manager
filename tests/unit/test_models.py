"""Test models."""
from pathlib import Path

import hcl  # type: ignore[import]
from faker import Faker

from boostsec.terraform_manager.models import (
    Tfvars,
    add_organization,
    Branding,
    add_feature_flag,
)
from boostsec.terraform_manager.testing.factories import (
    TfvarsFactory,
    OrganizationFactory,
)


def test_load_tfvars() -> None:
    """Test loading tfvars file."""
    tfvars_hcl = hcl.loads(
        (Path(__file__).parent.parent / "data/auth0.tfvars").read_text()
    )
    variables = Tfvars.parse_raw(hcl.dumps(tfvars_hcl))
    assert len(variables.organizations) > 10


def test_add_organization(faker: Faker) -> None:
    """Test adding an organization."""
    before_org_name = faker.pystr()
    before_orgs = {before_org_name: OrganizationFactory.build()}
    model: Tfvars = TfvarsFactory.build(organizations=before_orgs)
    display_name = faker.pystr()
    org_name = faker.pystr()

    new_model = add_organization(model, org_name=org_name, display_name=display_name)
    assert new_model.organizations[before_org_name] == before_orgs[before_org_name]

    assert new_model.organizations[org_name].display_name == display_name


def test_add_organization_with_optionals(faker: Faker) -> None:
    """Test adding an organization with optional args."""
    before_org_name = faker.pystr()
    before_orgs = {before_org_name: OrganizationFactory.build()}
    model: Tfvars = TfvarsFactory.build(organizations=before_orgs)

    display_name = faker.pystr()
    org_name = faker.pystr()
    features = [faker.pystr()]
    branding = Branding()
    connections = {faker.pystr(): faker.pybool()}
    connection_ids = [faker.pystr()]
    conn_defaults = faker.pybool()

    new_model = add_organization(
        model,
        org_name=org_name,
        display_name=display_name,
        features=features,
        branding=branding,
        connections=connections,
        connection_ids=connection_ids,
        conn_defaults=conn_defaults,
    )
    assert new_model.organizations[before_org_name] == before_orgs[before_org_name]
    new_org = new_model.organizations[org_name]

    assert new_org.display_name == display_name
    assert new_org.boost_org_features == features
    assert new_org.branding == branding
    assert new_org.connections == connections
    assert new_org.connection_ids == connection_ids
    assert new_org.conn_defaults == conn_defaults


def test_add_feature_flag(faker: Faker) -> None:
    """"""
    before_org_names = [faker.pystr(), faker.pystr()]
    before_features = [[faker.pystr()], [faker.pystr()]]

    before_orgs = {
        before_org_names[0]: OrganizationFactory.build(
            boost_org_features=before_features[0]
        ),
        before_org_names[1]: OrganizationFactory.build(
            boost_org_features=before_features[1]
        ),
    }
    feature_flag = faker.pystr()
    model: Tfvars = TfvarsFactory.build(organizations=before_orgs)
    new_model = add_feature_flag(feature_flag=feature_flag, model=model)
    assert len(new_model.organizations) == 2
    assert new_model.organizations[before_org_names[0]].boost_org_features == [
        *before_features[0],
        feature_flag,
    ]
    assert new_model.organizations[before_org_names[1]].boost_org_features == [
        *before_features[1],
        feature_flag,
    ]
