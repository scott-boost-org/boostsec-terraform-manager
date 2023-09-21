import hcl

from terraform_manager.models import Tfvars


def test_load_tfvars():
    """Test loading tfvars file"""
    with open("data/auth0.tfvars", 'r') as f:
        tfvars_hcl = hcl.load(f)
    vars = Tfvars.model_validate_json(hcl.dumps(tfvars_hcl))
    assert len(vars.organizations) > 10
