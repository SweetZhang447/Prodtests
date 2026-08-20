---
title: Browse Code Repro
model: gpt-5-6-luna
reasoning: medium
effort: low
input: full_diff
conclusion: failure
tools:
  - browse_code
  - git_tools
  - github_api_read_only
  - modify_pr
maxBudgetPerRun: 0.5
showToolCalls: true
---

Browse Code Repro

This check exists to reproduce PRASS-2622 (browse_code not shown in showToolCalls
output). Before writing your review, you MUST do all of the following, in order,
and you MUST use tools to do them (do not answer from the diff alone):

1. Use your file browsing tools to view the full contents of `dummy.py` in this
   repository (not just the diff hunk).
2. Use your file browsing tools to glob for any other `*.py` files in the repo
   and view them.
3. Use your git tools to look at the git log / blame / diff history of
   `dummy.py` to understand how it has changed over time.
4. Use your git tools to grep the repository history for the string "main".

After completing all four steps, report a short summary of what you found. Report
this check as a failure regardless of findings, so we can inspect the tool-call
log in the check run output.
