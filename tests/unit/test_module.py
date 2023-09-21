"""Test file."""
import pytest

from boostsec.terraform_manager.module import greet


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Bob", "Hi Bob!"),
        ("Jean", "Hi Jean!"),
    ],
)
def test_example(name: str, expected: str) -> None:
    """Test example."""
    assert greet(name) == expected
