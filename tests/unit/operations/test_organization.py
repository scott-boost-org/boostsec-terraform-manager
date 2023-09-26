"""Test."""
from faker import Faker

from boostsec.terraform_manager.models import (
    Branding,
    Tfvars,
)
from boostsec.terraform_manager.operations.organization import (
    add_feature_flag_for_orgs,
    add_organization,
)
from boostsec.terraform_manager.testing.factories import (
    OrganizationFactory,
    TfvarsFactory,
)


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


def test_add_feature_flag_for_all_orgs(faker: Faker) -> None:
    """Test add feature flag for all orgs."""
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
    new_model = add_feature_flag_for_orgs(feature_flag=feature_flag, model=model)
    assert len(new_model.organizations) == 2
    assert new_model.organizations[before_org_names[0]].boost_org_features == [
        *before_features[0],
        feature_flag,
    ]
    assert new_model.organizations[before_org_names[1]].boost_org_features == [
        *before_features[1],
        feature_flag,
    ]
