---
waitsFor:
  - "testingwait"
waitsForDiscoveryTimeout: 2
---
Debounce test (PRASS-2214 workaround): correctness waits up to 2 minutes for a nonexistent "testingwait" check.
