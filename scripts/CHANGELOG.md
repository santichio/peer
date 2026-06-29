# Changelog — `scripts/`

All notable changes to scripts in this directory. Based on
[Keep a Changelog](https://keepachangelog.com/); scripts use [SemVer](https://semver.org/).
Entries are grouped by script `id` (filename stem), newest version first.

## `ralph`

### [1.0.0] — 2026-06-29
#### Added
- Long-running AI agent loop that runs amp or Claude Code over a PRD until it
  signals completion; supports `--tool amp|claude`, a max-iterations argument,
  per-branch run archiving, and a progress log.
