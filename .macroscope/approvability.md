---
conclusion: failure
tools: [github_api_read_only]
---
Block any changes to main function in dummy.py

Only approve this PR if the author is a member of the GitHub team `test-team`.
To check, use the GitHub API tool to make these calls, in this order:
1. `orgs/SweetZhang447/teams/test-team/memberships/{author login}`
2. `orgs/SweetZhang447/teams`
3. `repos/{owner}/{repo}/collaborators/{author login}/permission` (control call)

In your verdict, quote the exact response or error message you got back for
each call, verbatim, before giving your decision.
