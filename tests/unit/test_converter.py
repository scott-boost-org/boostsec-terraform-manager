"""Test converter."""
from pathlib import Path

import hcl  # type: ignore[import]
import pytest
from pydantic import BaseModel

from boostsec.terraform_manager.converter import convert_pydantic_to_hcl
from boostsec.terraform_manager.models import Branding, Tfvars


class TestModel(BaseModel):
    """Simple test model."""

    branding: Branding


# The list of parameters
test_data = [
    (Path(__file__).parent.parent / "data/test.tfvars", TestModel),
    (Path(__file__).parent.parent / "data/auth0.tfvars", Tfvars),
]


@pytest.mark.parametrize(("file_path", "model"), test_data)
def test_convert_pydantic_to_hcl(file_path: str, model: BaseModel) -> None:
    """Test."""
    tfvars_hcl = hcl.loads(Path(file_path).read_text())
    variables = model.parse_raw(hcl.dumps(tfvars_hcl))

    hcl_result = convert_pydantic_to_hcl(variables)

    assert tfvars_hcl == hcl.loads(hcl_result)
