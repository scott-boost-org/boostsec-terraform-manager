"""Test."""
import pytest
from faker import Faker
from requests_mock import Mocker

from boostsec.terraform_manager.operations.github import Workspace, create_pr
from boostsec.terraform_manager.testing.payloads.github import (
    get_branch_response,
    get_content_response,
    get_create_file_response,
    get_create_pull_request_response,
    get_repo_response,
)


@pytest.mark.parametrize("workspace", list(Workspace))
def test_create_pr(requests_mock: Mocker, workspace: Workspace, faker: Faker) -> None:
    """Should create pr."""
    file_content = faker.pystr()
    branch_name = faker.pystr()
    default_branch = faker.pystr()
    faker.pystr()
    commit_msg = faker.pystr()
    pr_title = faker.pystr()
    token = faker.pystr()

    requests_mock.get(
        "/repos/boostsecurityio/terraform-releases",
        json=get_repo_response(
            org="boostsecurityio",
            repo="terraform-releases",
            default_branch=default_branch,
        ),
    )
    requests_mock.get(
        f"/repos/boostsecurityio/terraform-releases/branches/{default_branch}",
        json=get_branch_response(),
    )
    requests_mock.post(
        "/repos/boostsecurityio/terraform-releases/git/refs",
        json=get_branch_response(),
    )
    requests_mock.get(
        f"/repos/boostsecurityio/terraform-releases/contents/workspaces/{workspace.value}/02-auth0/terraform.auto.tfvars?ref={branch_name}",
        json=get_content_response(),
    )
    requests_mock.put(
        f"/repos/boostsecurityio/terraform-releases/contents/workspaces/{workspace.value}/02-auth0/terraform.auto.tfvars",
        json=get_create_file_response(),
    )
    requests_mock.post(
        "/repos/boostsecurityio/terraform-releases/pulls",
        json=get_create_pull_request_response(),
    )

    create_pr(
        file_content=file_content,
        branch_name=branch_name,
        commit_msg=commit_msg,
        pr_title=pr_title,
        token=token,
        workspace=workspace,
    )
