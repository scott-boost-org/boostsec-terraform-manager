"""Test models."""
from pathlib import Path

import hcl  # type: ignore[import]

from boostsec.terraform_manager.models import Tfvars


def test_load_tfvars() -> None:
    """Test loading tfvars file."""
    tfvars_hcl = hcl.loads(Path("../data/auth0.tfvars").read_text())
    variables = Tfvars.parse_raw(hcl.dumps(tfvars_hcl))
    assert len(variables.organizations) > 10
