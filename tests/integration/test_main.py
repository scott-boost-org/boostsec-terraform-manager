"""Test main.py."""
from typer.testing import CliRunner

from boostsec.terraform_manager.main import app

runner = CliRunner()


def test_version() -> None:
    """Test version command."""
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "Version 0.0.1" in result.stdout


def test_update() -> None:
    """Test update command."""
    result = runner.invoke(app, ["update"])
    assert result.exit_code == 0
    assert "Update an org" in result.stdout


def test_create() -> None:
    """Test create command."""
    result = runner.invoke(app, ["create"])
    assert result.exit_code == 0
    assert "Create an org" in result.stdout


def test_delete() -> None:
    """Test delete command."""
    result = runner.invoke(app, ["delete"])
    assert result.exit_code == 0
    assert "Delete an org" in result.stdout
