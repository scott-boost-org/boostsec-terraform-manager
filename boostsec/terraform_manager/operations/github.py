"""GitHub operations."""
from enum import Enum
from pathlib import Path
from typing import cast

from github import Github
from github.ContentFile import ContentFile
from github.Repository import Repository


class Workspace(str, Enum):
    """Types of workspaces."""

    DEV = "dev"
    PROD = "prod-use2"


AUTH0_PATH = "workspaces/{workspace}/02-auth0/terraform.auto.tfvars"


def _get_repo(token: str) -> Repository:
    client = Github(token)
    return client.get_repo("boostsecurityio/terraform-releases")


def _create_branch(repository: Repository, branch_name: str) -> None:
    default_branch = repository.get_branch(repository.default_branch)

    repository.create_git_ref(
        ref=f"refs/heads/{branch_name}",
        sha=default_branch.commit.sha,
    )


def _update_file(
    repository: Repository,
    path: Path,
    commit_msg: str,
    content: str,
    branch_name: str,
) -> None:
    content_file: ContentFile = cast(
        ContentFile,
        repository.get_contents(path=str(path), ref=branch_name),
    )
    repository.update_file(
        path=str(path),
        message=commit_msg,
        content=content,
        branch=branch_name,
        sha=content_file.sha,
    )


def create_pr(
    file_content: str,
    branch_name: str,
    commit_msg: str,
    pr_title: str,
    token: str,
    workspace: Workspace,
) -> None:
    """Create a Pull Request."""
    repo = _get_repo(token)
    _create_branch(
        repository=repo,
        branch_name=branch_name,
    )
    _update_file(
        repository=repo,
        path=Path(AUTH0_PATH.format(workspace=workspace)),
        commit_msg=commit_msg,
        content=file_content,
        branch_name=branch_name,
    )
    pr = repo.create_pull(
        title=pr_title,
        body=commit_msg,
        head=branch_name,
        base=repo.default_branch,
    )
    print(pr.html_url)
