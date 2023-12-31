"""Entrypoint."""
from pathlib import Path

import hcl  # type: ignore
import typer

from boostsec.terraform_manager.models import Tfvars
from boostsec.terraform_manager.operations.github import (
    AUTH0_PATH,
    Workspace,
    create_pr,
)
from boostsec.terraform_manager.operations.organization import (
    add_feature_flag_for_orgs,
    add_organization,
)
from boostsec.terraform_manager.utils.converter import (
    convert_pydantic_to_hcl,
    format_terraform_code,
)

app = typer.Typer()

list_option = typer.Option("", help="List of orgs to update separated by comma")
github_token_env = typer.Argument("None", envvar=["GITHUB_TOKEN"])
terraform_location = typer.Argument("None", envvar=["GITHUB_WORKSPACE"])


@app.command()
def version() -> None:
    """Version."""
    typer.echo("Version 0.0.1")


@app.command()
def create(
    org_name: str,
    display_name: str,
    workspace: Workspace,
    location: str = terraform_location,
    gh_api_token: str = github_token_env,
) -> None:
    """Create."""
    tfvars_hcl = hcl.loads(
        Path(f"{location}/{AUTH0_PATH.format(workspace=workspace)}").read_text()
    )
    variables = Tfvars.parse_raw(hcl.dumps(tfvars_hcl))

    new_org_vars = add_organization(
        variables,
        org_name=org_name,
        display_name=display_name,
    )

    hcl_result = convert_pydantic_to_hcl(new_org_vars)

    formatted_result = format_terraform_code(hcl_result)

    create_pr(
        file_content=formatted_result,
        branch_name=f"create-{workspace}-{org_name}",
        commit_msg=f"Add {display_name} to {workspace} environment",
        pr_title=f"[{workspace.upper()}] Create {display_name}",
        token=gh_api_token,
        workspace=workspace,
    )


@app.command()
def update(
    feature_flag: str,
    workspace: Workspace,
    orgs: str = list_option,
    location: str = terraform_location,
    gh_api_token: str = github_token_env,
) -> None:
    """Update."""
    org_list = [org.strip() for org in orgs.split(",") if org]

    tfvars_hcl = hcl.loads(
        Path(f"{location}/{AUTH0_PATH.format(workspace=workspace)}").read_text()
    )
    variables = Tfvars.parse_raw(hcl.dumps(tfvars_hcl))

    new_org_vars = add_feature_flag_for_orgs(feature_flag, variables, orgs=org_list)

    hcl_result = convert_pydantic_to_hcl(new_org_vars)

    formatted_result = format_terraform_code(hcl_result)

    create_pr(
        file_content=formatted_result,
        branch_name=f"update-{workspace}-{feature_flag}",
        commit_msg=(
            f"Add {feature_flag} to "
            f"{'all orgs' if not org_list else orgs} "
            f"in the {workspace} environment"
        ),
        pr_title=(
            f"[{workspace.upper()}] "
            f"Update {'orgs' if not org_list else orgs} "
            f"with feature flag: {feature_flag}"
        ),
        token=gh_api_token,
        workspace=workspace,
    )


@app.command()
def delete() -> None:
    """Delete."""
    typer.echo("Delete an org")


if __name__ == "__main__":  # pragma: no cover
    app()
