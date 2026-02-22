# OPS-404: Investigate Production Incident from Logs

**Status:** In Progress · **Priority:** High
**Sprint:** Sprint 33 · **Story Points:** 5
**Reporter:** On-Call Team · **Assignee:** You (Intern)
**Labels:** `incident`, `debugging`, `logs`, `python`
**Task Type:** Debugging

---

## Description

A production incident occurred at 14:32 UTC. Users saw 500 errors for 12 minutes.
Parse the log file to find the root cause. The log parser has bugs that hide the answer.

## Acceptance Criteria

- [ ] Log parser correctly extracts timestamp, level, message
- [ ] Error log filtering works (shows only ERROR level)
- [ ] Timeline construction shows events in chronological order
- [ ] Root cause identified from log pattern
- [ ] All tests pass
