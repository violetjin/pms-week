# GitLab API notes (self-hosted)

Base: `https://<gitlab-host>/api/v4`
Auth header: `PRIVATE-TOKEN: <token>` (PAT)

## Common endpoints

- List group projects
  - `GET /groups/:id/projects?include_subgroups=true&per_page=100&page=1`

- List project commits
  - `GET /projects/:id/repository/commits?since=<iso>&until=<iso>&per_page=100&page=1`

- Commit detail (stats)
  - `GET /projects/:id/repository/commits/:sha`

- Commit diff
  - `GET /projects/:id/repository/commits/:sha/diff`

- Merge requests (optional)
  - `GET /projects/:id/merge_requests?scope=all&created_after=<iso>&created_before=<iso>`

## Pagination

GitLab uses `X-Next-Page`, `X-Page`, `X-Total-Pages` headers.

## Date/time

Use ISO 8601 UTC in API calls; convert from local timezone window.

## Identity mapping

Commit list items include `author_name`, `author_email`, `committer_name`, `committer_email`.
If you need GitLab user ids, use:
- Search users: `GET /users?search=<email or name>` (may require admin perms)

Prefer stable mapping: email → person.
