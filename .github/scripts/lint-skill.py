#!/usr/bin/env python3
"""Validate a single skills/<name>/SKILL.md file.

Used by .github/workflows/lint-skills.yml.

Usage:  lint-skill.py <path-to-SKILL.md> <expected-folder-name>
Exits non-zero on any violation; prints `::error file=...::` annotations.
"""

import pathlib
import re
import sys

import yaml


def main(path: str, expected: str) -> int:
    text = pathlib.Path(path).read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        print(f"::error file={path}::missing or malformed YAML frontmatter")
        return 1
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"::error file={path}::YAML parse error: {e}")
        return 1
    if not isinstance(fm, dict):
        print(f"::error file={path}::frontmatter is not a YAML mapping")
        return 1

    name = (fm.get("name") or "").strip()
    desc = (fm.get("description") or "").strip()
    failed = False
    if name != expected:
        print(
            f"::error file={path}::name='{name}' does not match folder '{expected}'"
        )
        failed = True
    if not desc:
        print(f"::error file={path}::description is missing or empty")
        failed = True
    if failed:
        return 1
    print(f"OK {path}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: lint-skill.py <path-to-SKILL.md> <expected-folder-name>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
