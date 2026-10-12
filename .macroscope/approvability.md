---
conclusion: failure
tools: [github_api_read_only]
---
Block any changes to main function in dummy.py

Only approve this PR if the person who opened it is a member of the
`test-team` GitHub team. Use the GitHub API to check their team membership.
If you can't confirm they're on the team, don't approve, and explain exactly
what you tried and what happened.
