#!/usr/bin/env python3
"""Count a UTF-8 prompt exactly as saved, without submitting it to an API."""

import argparse
import json
from pathlib import Path


def inspect_prompt(path, limit):
    # Preserve saved line endings; do not strip whitespace or Markdown fences.
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        text = handle.read()
    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    crlf_text = normalized.replace("\n", "\r\n")
    return {
        "characters": len(text),
        "characters_if_crlf": len(crlf_text),
        "utf8_bytes": len(text.encode("utf-8")),
        "limit": limit,
        "remaining": limit - len(text),
        "within_limit": len(text) <= limit,
        "within_limit_if_crlf": len(crlf_text) <= limit,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompt_file", type=Path)
    parser.add_argument("--limit", type=int, default=7000)
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()
    if args.limit <= 0:
        parser.error("--limit must be positive")
    try:
        report = inspect_prompt(args.prompt_file, args.limit)
    except (OSError, UnicodeError) as exc:
        parser.exit(2, f"Cannot read UTF-8 prompt: {exc}\n")
    if args.as_json:
        print(json.dumps(report, ensure_ascii=True))
    else:
        status = "PASS" if report["within_limit"] else "FAIL"
        print(f"{status}: {report['characters']} / {report['limit']} characters")
        print(f"Remaining: {report['remaining']}; with CRLF: {report['characters_if_crlf']}")
        if not report["within_limit_if_crlf"]:
            print("WARNING: CRLF line endings would exceed the limit; shorten the prompt.")
    return 0 if report["within_limit"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
