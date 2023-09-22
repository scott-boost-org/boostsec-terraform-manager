"""Payloads for GitHub responses."""
import os
from base64 import b64encode
from typing import Any, Optional

from faker import Faker

_faker = Faker()

BASE_URL = "https://api.github.com"


def _an_organization(
    base_url: Optional[str] = None, org: Optional[str] = None
) -> dict[str, Any]:
    org = org or _faker.pystr()
    return {
        "login": org,
        "id": 95301622,
        "node_id": "O_kgDOBa4v9g",
        "avatar_url": "https://avatars.githubusercontent.com/u/95301622?v=4",
        "gravatar_id": "",
        "url": f"{base_url}/users/{org}",
        "html_url": f"https://github.com/{org}",
        "followers_url": f"{base_url}/users/{org}/followers",
        "following_url": f"{base_url}/users/{org}/following{{/other_user}}",
        "gists_url": f"{base_url}/users/{org}/gists{{/gist_id}}",
        "starred_url": f"{base_url}/users/{org}/starred{{/owner}}{{/repo}}",
        "subscriptions_url": f"{base_url}/users/{org}/subscriptions",
        "organizations_url": f"{base_url}/users/{org}/orgs",
        "repos_url": f"{base_url}/users/{org}/repos",
        "events_url": f"{base_url}/users/{org}/events{{/privacy}}",
        "received_events_url": f"{base_url}/users/{org}/received_events",
        "type": "Organization",
        "site_admin": False,
    }


def get_repo_response(
    org: Optional[str] = None,
    repo: Optional[str] = None,
    default_branch: Optional[str] = None,
    base_url: Optional[str] = None,
) -> dict[str, Any]:
    """Create a response.

    https://api.github.com:443/repos/{org}/{repo}
    """
    base_url = base_url or BASE_URL
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    default_branch = default_branch or _faker.pystr()

    return {
        "id": 433492562,
        "node_id": "R_kgDOGdaSUg",
        "name": repo,
        "full_name": f"{org}/{repo}",
        "private": True,
        "owner": _an_organization(BASE_URL, org),
        "html_url": f"https://github.com/{org}/{repo}",
        "description": None,
        "fork": False,
        "url": f"{base_url}/repos/{org}/{repo}",
        "forks_url": f"{base_url}/repos/{org}/{repo}/forks",
        "keys_url": f"{base_url}/repos/{org}/{repo}/keys{{/key_id}}",
        "collaborators_url": (
            f"{base_url}/repos/{org}/{repo}/collaborators{{/collaborator}}"
        ),
        "teams_url": f"{base_url}/repos/{org}/{repo}/teams",
        "hooks_url": f"{base_url}/repos/{org}/{repo}/hooks",
        "issue_events_url": f"{base_url}/repos/{org}/{repo}/issues/events{{/number}}",
        "events_url": f"{base_url}/repos/{org}/{repo}/events",
        "assignees_url": f"{base_url}/repos/{org}/{repo}/assignees{{/user}}",
        "branches_url": f"{base_url}/repos/{org}/{repo}/branches{{/branch}}",
        "tags_url": f"{base_url}/repos/{org}/{repo}/tags",
        "blobs_url": f"{base_url}/repos/{org}/{repo}/git/blobs{{/sha}}",
        "git_tags_url": f"{base_url}/repos/{org}/{repo}/git/tags{{/sha}}",
        "git_refs_url": f"{base_url}/repos/{org}/{repo}/git/refs{{/sha}}",
        "trees_url": f"{base_url}/repos/{org}/{repo}/git/trees{{/sha}}",
        "statuses_url": f"{base_url}/repos/{org}/{repo}/statuses/{{sha}}",
        "languages_url": f"{base_url}/repos/{org}/{repo}/languages",
        "stargazers_url": f"{base_url}/repos/{org}/{repo}/stargazers",
        "contributors_url": f"{base_url}/repos/{org}/{repo}/contributors",
        "subscribers_url": f"{base_url}/repos/{org}/{repo}/subscribers",
        "subscription_url": f"{base_url}/repos/{org}/{repo}/subscription",
        "commits_url": f"{base_url}/repos/{org}/{repo}/commits{{/sha}}",
        "git_commits_url": f"{base_url}/repos/{org}/{repo}/git/commits{{/sha}}",
        "comments_url": f"{base_url}/repos/{org}/{repo}/comments{{/number}}",
        "issue_comment_url": (
            f"{base_url}/repos/{org}/{repo}/issues/comments{{/number}}"
        ),
        "contents_url": f"{base_url}/repos/{org}/{repo}/contents/{{+path}}",
        "compare_url": f"{base_url}/repos/{org}/{repo}/compare/{{base}}...{{head}}",
        "merges_url": f"{base_url}/repos/{org}/{repo}/merges",
        "archive_url": f"{base_url}/repos/{org}/{repo}/{{archive_format}}{{/ref}}",
        "downloads_url": f"{base_url}/repos/{org}/{repo}/downloads",
        "issues_url": f"{base_url}/repos/{org}/{repo}/issues{{/number}}",
        "pulls_url": f"{base_url}/repos/{org}/{repo}/pulls{{/number}}",
        "milestones_url": f"{base_url}/repos/{org}/{repo}/milestones{{/number}}",
        "notifications_url": (
            f"{base_url}/repos/{org}/{repo}/notifications{{?since,all,participating}}"
        ),
        "labels_url": f"{base_url}/repos/{org}/{repo}/labels{{/name}}",
        "releases_url": f"{base_url}/repos/{org}/{repo}/releases{{/id}}",
        "deployments_url": f"{base_url}/repos/{org}/{repo}/deployments",
        "created_at": "2021-11-30T15:55:00Z",
        "updated_at": "2021-11-30T15:55:00Z",
        "pushed_at": "2022-01-27T21:52:43Z",
        "git_url": f"git://github.com/{org}/{repo}.git",
        "ssh_url": f"git@github.com:{org}/{repo}.git",
        "clone_url": f"https://github.com/{org}/{repo}.git",
        "svn_url": f"https://github.com/{org}/{repo}",
        "homepage": None,
        "size": 0,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": None,
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 0,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": None,
        "allow_forking": False,
        "is_template": False,
        "topics": [],
        "visibility": "private",
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": default_branch,
        "permissions": {
            "admin": False,
            "maintain": False,
            "push": False,
            "triage": False,
            "pull": False,
        },
        "temp_clone_token": "...",
        "allow_squash_merge": True,
        "allow_merge_commit": True,
        "allow_rebase_merge": True,
        "allow_auto_merge": False,
        "delete_branch_on_merge": False,
        "allow_update_branch": False,
        "organization": _an_organization(base_url, org),
        "network_count": 0,
        "subscribers_count": 1,
    }


def get_branch_response(
    org: Optional[str] = None,
    repo: Optional[str] = None,
    branch_name: Optional[str] = None,
    base_url: Optional[str] = None,
    branch_protection_enabled: bool = False,
    head_sha: Optional[str] = None,
) -> dict[str, Any]:
    """Create a response.

    https://api.github.com:443/repos/{org}/{repo}/branches/{branch}
    """
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    branch_name = branch_name or _faker.pystr()
    base_url = base_url or BASE_URL

    return {
        "name": branch_name,
        "commit": _a_commit(sha=head_sha),
        "_links": {
            "self": f"https://{base_url}/repos/{org}/{repo}/branches/{branch_name}",
            "html": f"https://github.com/{org}/{repo}/tree/{branch_name}",
        },
        "protected": branch_protection_enabled,
        "protection": _a_protection_status(enabled=branch_protection_enabled),
        "protection_url": f"https://{base_url}/repos/{org}/{repo}/branches/"
        f"{branch_name}/protection",
    }


def _a_commit(
    user_id: Optional[int] = None,
    login: Optional[str] = None,
    org: Optional[str] = None,
    repo: Optional[str] = None,
    base_url: Optional[str] = None,
    sha: Optional[str] = None,
    parent_sha: Optional[str] = None,
) -> dict[str, Any]:
    user = _a_user(user_id, login, base_url)
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    sha = sha or _faker.sha1()
    parent_sha = parent_sha or _faker.sha1()
    tree_sha = _faker.sha1()

    return {
        "sha": sha,
        "node_id": _faker.pystr(),
        "commit": {
            "author": {
                "name": "Monalisa Octocat",
                "email": "octocat@github.com",
                "date": "2022-10-20T17:40:46Z",
            },
            "committer": {
                "name": "Monalisa Octocat",
                "email": "octocat@github.com",
                "date": "2022-10-20T17:40:46Z",
            },
            "message": "Test",
            "tree": {
                "sha": tree_sha,
                "url": f"https://{base_url}/repos/{org}/{repo}/git/trees/{tree_sha}",
            },
            "url": f"https://{base_url}/repos/{org}/{repo}/git/commits/{sha}",
            "comment_count": 0,
            "verification": {
                "verified": None,
                "reason": "unsigned",
                "signature": None,
                "payload": None,
            },
        },
        "url": f"https://{base_url}/repos/{org}/{repo}/commits/{sha}",
        "html_url": f"https://github.com/{org}/{repo}/commit/{sha}",
        "comments_url": f"https://{base_url}/repos/{org}/{repo}/commits/{sha}/comments",
        "author": user,
        "committer": user,
        "parents": [
            {
                "sha": parent_sha,
                "url": f"https://{base_url}/repos/{org}/{repo}/commits/{parent_sha}",
                "html_url": f"https://github.com/{org}/{repo}/commit/{parent_sha}",
            }
        ],
    }


def _a_user(
    user_id: Optional[int] = None,
    login: Optional[str] = None,
    base_url: Optional[str] = None,
) -> dict[str, Any]:
    user_id = user_id if user_id is not None else _faker.pyint(min_value=1)
    login = login or _faker.pystr()
    base_url = base_url or BASE_URL

    return {
        "login": login,
        "id": user_id,
        "node_id": _faker.pystr(),
        "avatar_url": f"https://avatars.githubusercontent.com/u/{user_id}?v=4",
        "gravatar_id": "",
        "url": f"https://{base_url}/users/{login}",
        "html_url": f"https://github.com/{login}",
        "followers_url": f"https://{base_url}/users/{login}/followers",
        "following_url": f"https://{base_url}/users/{login}/following" "{/other_user}",
        "gists_url": f"https://{base_url}/users/{login}/gists{{/gist_id}}",
        "starred_url": f"https://{base_url}/users/{login}/starred{{/owner}}" "{/repo}",
        "subscriptions_url": f"https://{base_url}/users/{login}/subscriptions",
        "organizations_url": f"https://{base_url}/users/{login}/orgs",
        "repos_url": f"https://{base_url}/users/{login}/repos",
        "events_url": f"https://{base_url}/users/{login}/events{{/privacy}}",
        "received_events_url": f"https://{base_url}/users/{login}" "/received_events",
        "type": "User",
        "site_admin": False,
    }


def _a_protection_status(enabled: bool = True) -> dict[str, Any]:
    return {
        "enabled": enabled,
        "required_status_checks": {
            "enforcement_level": "off",
            "contexts": [],
            "checks": [],
        },
    }


def get_content_response(
    file_path: Optional[str] = None,
    file_data: Optional[str] = None,
    file_sha: Optional[str] = None,
    org: Optional[str] = None,
    repo: Optional[str] = None,
    branch_name: Optional[str] = None,
    base_url: Optional[str] = None,
) -> dict[str, Any]:
    """Create a "get file" response.

    GET https://api.github.com:443/repos/{org}/{repo}/contents/{path}
    """
    file_path = file_path or _faker.file_path(depth=3, absolute=False)
    file_data = file_data or _faker.pystr()
    file_sha = file_sha or _faker.pystr()
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    branch_name = branch_name or _faker.pystr()
    base_url = base_url or BASE_URL

    return _a_content_response(
        file_path=file_path,
        file_data=file_data,
        file_sha=file_sha,
        org=org,
        repo=repo,
        branch_name=branch_name,
        base_url=base_url,
    )


def _a_content_response(
    file_path: Optional[str] = None,
    file_data: Optional[str] = None,
    file_sha: Optional[str] = None,
    org: Optional[str] = None,
    repo: Optional[str] = None,
    branch_name: Optional[str] = None,
    base_url: Optional[str] = None,
) -> dict[str, Any]:
    file_path = file_path or _faker.file_path(depth=3, absolute=False)
    file_sha = file_sha or _faker.sha1()
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    branch_name = branch_name or _faker.pystr()
    base_url = base_url or BASE_URL

    file_name = os.path.basename(file_path)

    content = {
        "name": file_name,
        "path": file_path,
        "sha": file_sha,
        "size": _faker.pyint(),
        "url": f"https://{base_url}/repos/{org}/{repo}/contents/{file_path}"
        f"/?ref={branch_name}",
        "html_url": f"https://github.com/{org}/{repo}/blob/master/{file_path}/",
        "git_url": f"https://{base_url}/repos/{org}/{repo}/git/blobs/{file_sha}",
        "download_url": f"https://raw.githubusercontent.com/{org}/{repo}"
        f"/{branch_name}/{file_path}/",
        "type": "file",
        "_links": {
            "self": f"https://{base_url}/repos/{org}/{repo}/contents/{file_path}"
            f"/?ref={branch_name}",
            "git": f"https://{base_url}/repos/{org}/{repo}/git/blobs/{file_sha}",
            "html": (
                f"https://github.com/{org}/{repo}/blob/{branch_name}/{file_path}/"
            ),
        },
    }

    if file_data:
        encoded_file = b64encode(file_data.encode()).decode()

        content.update({"content": encoded_file, "encoding": "base64"})

    return content


def get_create_file_response(
    file_path: Optional[str] = None,
    org: Optional[str] = None,
    repo: Optional[str] = None,
    branch_name: Optional[str] = None,
    base_url: Optional[str] = None,
    commit_sha: Optional[str] = None,
) -> dict[str, Any]:
    """Create a "create file" response.

    PUT https://api.github.com:443/repos/{org}/{repo}/contents/{path}
    """
    file_path = file_path or _faker.file_path(depth=3, absolute=False)
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    branch_name = branch_name or _faker.pystr()
    base_url = base_url or BASE_URL
    commit_sha = commit_sha or _faker.sha1()

    return {
        "content": _a_content_response(
            file_path=file_path,
            org=org,
            repo=repo,
            branch_name=branch_name,
            base_url=base_url,
        ),
        "commit": _a_commit(org=org, repo=repo, base_url=base_url, sha=commit_sha),
    }


def get_create_pull_request_response(
    org: Optional[str] = None,
    repo: Optional[str] = None,
    base_url: Optional[str] = None,
    title: Optional[str] = None,
    body: Optional[str] = None,
    number: Optional[int] = None,
    head_branch_name: Optional[str] = None,
    head_sha: Optional[str] = None,
    base_branch_name: Optional[str] = None,
    base_sha: Optional[str] = None,
    state: Optional[str] = None,
) -> dict[str, Any]:
    """Create a response.

    https://api.github.com:443/repos/{org}/{repo}/pulls
    """
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    base_url = base_url or BASE_URL
    title = title or _faker.pystr()
    body = body or _faker.pystr()
    number = number if number is not None else _faker.pyint(min_value=1)
    head_branch_name = head_branch_name or _faker.pystr()
    head_sha = head_sha or _faker.sha1()
    base_branch_name = base_branch_name or _faker.pystr()
    base_sha = base_sha or _faker.sha1()
    state = state or "open"

    return {
        "url": f"{base_url}/repos/{org}/{repo}/pulls/{number}",
        "id": _faker.pyint(),
        "node_id": "PR_gfdrh3904gfdsklI",
        "html_url": f"https://github.com/{org}/{repo}/pull/{number}",
        "diff_url": f"https://github.com/{org}/{repo}/pull/{number}.diff",
        "patch_url": f"https://github.com/{org}/{repo}/pull/{number}.patch",
        "issue_url": f"{base_url}/repos/{org}/{repo}/issues/{number}",
        "number": number,
        "state": state,
        "locked": False,
        "title": title,
        "user": _a_user(base_url=base_url),
        "body": body,
        "created_at": "2022-11-03T17:41:28Z",
        "updated_at": "2022-11-03T17:41:28Z",
        "closed_at": None,
        "merged_at": None,
        "merge_commit_sha": None,
        "assignee": None,
        "assignees": [],
        "requested_reviewers": [],
        "requested_teams": [],
        "labels": [],
        "milestone": None,
        "draft": False,
        "commits_url": f"{base_url}/repos/{org}/{repo}/pulls/{number}/commits",
        "review_comments_url": f"{base_url}/repos/{org}/{repo}/pulls/{number}/comments",
        "review_comment_url": f"{base_url}/repos/{org}/{repo}/pulls"
        "/comments{/number}",
        "comments_url": f"{base_url}/repos/{org}/{repo}/issues/{number}/comments",
        "statuses_url": f"{base_url}/repos/{org}/{repo}/statuses/{head_sha}",
        "head": _a_pull_request_reference(
            org, repo, base_url, head_branch_name, head_sha
        ),
        "base": _a_pull_request_reference(
            org, repo, base_url, base_branch_name, base_sha
        ),
        "_links": {
            "self": {"href": f"{base_url}/repos/{org}/{repo}/pulls/{number}"},
            "html": {"href": f"https://github.com/{org}/{repo}/pull/{number}"},
            "issue": {"href": f"{base_url}/repos/{org}/{repo}/issues/{number}"},
            "comments": {
                "href": f"{base_url}/repos/{org}/{repo}/issues/{number}/comments"
            },
            "review_comments": {
                "href": f"{base_url}/repos/{org}/{repo}/pulls/{number}/comments"
            },
            "review_comment": {
                "href": f"{base_url}/repos/{org}/{repo}/pulls/comments{{/number}}"
            },
            "commits": {
                "href": f"{base_url}/repos/{org}/{repo}/pulls/{number}/commits"
            },
            "statuses": {"href": f"{base_url}/repos/{org}/{repo}/statuses/{head_sha}"},
        },
        "author_association": "CONTRIBUTOR",
        "auto_merge": None,
        "active_lock_reason": None,
        "merged": False,
        "mergeable": None,
        "rebaseable": None,
        "mergeable_state": "unknown",
        "merged_by": None,
        "comments": 0,
        "review_comments": 0,
        "maintainer_can_modify": False,
        "commits": 1,
        "additions": 1,
        "deletions": 0,
        "changed_files": 1,
    }


def _a_pull_request_reference(
    org: Optional[str] = None,
    repo: Optional[str] = None,
    base_url: Optional[str] = None,
    branch_name: Optional[str] = None,
    sha: Optional[str] = None,
) -> dict[str, Any]:
    org = org or _faker.pystr()
    repo = repo or _faker.pystr()
    base_url = base_url or _faker.pystr()
    branch_name = branch_name or _faker.pystr()
    sha = sha or _faker.sha1()
    return {
        "label": f"{org}:{branch_name}",
        "ref": branch_name,
        "sha": sha,
        "user": _a_user(),
        "repo": {
            "id": 557949993,
            "node_id": "R_kgDOIUGkKQ",
            "name": f"{repo}",
            "full_name": f"{org}/{repo}",
            "private": True,
            "owner": _a_user(login=org),
            "html_url": f"https://github.com/{org}/{repo}",
            "description": None,
            "fork": False,
            "url": f"{base_url}/repos/{org}/{repo}",
            "forks_url": f"{base_url}/repos/{org}/{repo}/forks",
            "keys_url": f"{base_url}/repos/{org}/{repo}/keys{{/key_id}}",
            "collaborators_url": f"{base_url}/repos/{org}/{repo}"
            "/collaborators{/collaborator}",
            "teams_url": f"{base_url}/repos/{org}/{repo}/teams",
            "hooks_url": f"{base_url}/repos/{org}/{repo}/hooks",
            "issue_events_url": f"{base_url}/repos/{org}/{repo}/issues"
            "/events{/number}",
            "events_url": f"{base_url}/repos/{org}/{repo}/events",
            "assignees_url": f"{base_url}/repos/{org}/{repo}/assignees{{/user}}",
            "branches_url": f"{base_url}/repos/{org}/{repo}/branches{{/branch}}",
            "tags_url": f"{base_url}/repos/{org}/{repo}/tags",
            "blobs_url": f"{base_url}/repos/{org}/{repo}/git/blobs{{/sha}}",
            "git_tags_url": f"{base_url}/repos/{org}/{repo}/git/tags{{/sha}}",
            "git_refs_url": f"{base_url}/repos/{org}/{repo}/git/refs{{/sha}}",
            "trees_url": f"{base_url}/repos/{org}/{repo}/git/trees{{/sha}}",
            "statuses_url": f"{base_url}/repos/{org}/{repo}/statuses/{sha}",
            "languages_url": f"{base_url}/repos/{org}/{repo}/languages",
            "stargazers_url": f"{base_url}/repos/{org}/{repo}/stargazers",
            "contributors_url": f"{base_url}/repos/{org}/{repo}/contributors",
            "subscribers_url": f"{base_url}/repos/{org}/{repo}/subscribers",
            "subscription_url": f"{base_url}/repos/{org}/{repo}/subscription",
            "commits_url": f"{base_url}/repos/{org}/{repo}/commits{{/sha}}",
            "git_commits_url": f"{base_url}/repos/{org}/{repo}/git/commits{{/sha}}",
            "comments_url": f"{base_url}/repos/{org}/{repo}/comments{{/number}}",
            "issue_comment_url": f"{base_url}/repos/{org}/{repo}/issues"
            "/comments{/number}",
            "contents_url": f"{base_url}/repos/{org}/{repo}/contents/{{+path}}",
            "compare_url": f"{base_url}/repos/{org}/{repo}/compare/{{base}}...{{head}}",
            "merges_url": f"{base_url}/repos/{org}/{repo}/merges",
            "archive_url": f"{base_url}/repos/{org}/{repo}/{{archive_format}}{{/ref}}",
            "downloads_url": f"{base_url}/repos/{org}/{repo}/downloads",
            "issues_url": f"{base_url}/repos/{org}/{repo}/issues{{/number}}",
            "pulls_url": f"{base_url}/repos/{org}/{repo}/pulls{{/number}}",
            "milestones_url": f"{base_url}/repos/{org}/{repo}/milestones{{/number}}",
            "notifications_url": f"{base_url}/repos/{org}/{repo}"
            "/notifications{?since,all,participating}",
            "labels_url": f"{base_url}/repos/{org}/{repo}/labels{{/name}}",
            "releases_url": f"{base_url}/repos/{org}/{repo}/releases{{/id}}",
            "deployments_url": f"{base_url}/repos/{org}/{repo}/deployments",
            "created_at": "2022-10-26T15:55:13Z",
            "updated_at": "2022-10-26T15:55:13Z",
            "pushed_at": "2022-11-03T17:05:52Z",
            "git_url": f"git://github.com/{org}/{repo}.git",
            "ssh_url": f"git@github.com:{org}/{repo}.git",
            "clone_url": f"https://github.com/{org}/{repo}.git",
            "svn_url": f"https://github.com/{org}/{repo}",
            "homepage": None,
            "size": 0,
            "stargazers_count": 0,
            "watchers_count": 0,
            "language": None,
            "has_issues": True,
            "has_projects": True,
            "has_downloads": True,
            "has_wiki": True,
            "has_pages": False,
            "forks_count": 0,
            "mirror_url": None,
            "archived": False,
            "disabled": False,
            "open_issues_count": 1,
            "license": None,
            "allow_forking": False,
            "is_template": False,
            "web_commit_signoff_required": False,
            "topics": [],
            "visibility": "private",
            "forks": 0,
            "open_issues": 1,
            "watchers": 0,
            "default_branch": "main",
        },
    }
