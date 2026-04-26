#!/usr/bin/env python3
"""
pre-bash-guard.py — Claude Code PreToolUse hook

Blocks unambiguously destructive shell commands as a deterministic
safety net. Wired into .claude/settings.json under hooks.PreToolUse
with matchers "Bash" and "PowerShell".

Patterns blocked:
- rm -rf targeting root, home, wildcards, or system-level paths
  (specific paths inside the repo are allowed)
- git push --force without --force-with-lease
- git reset --hard
- Windows disk format / del /f /s / rd /s /q
- dd / mkfs disk-write commands
- chmod 777 on root or system paths

Day-to-day deletions of specific files (rm -rf node_modules, rm -rf
dist, etc.) are not blocked. The goal is to catch the catastrophic
patterns, not to be paranoid about routine operations.

To bypass for an intentional case, run the command in a separate
terminal outside Claude Code.

Spec: docs/website-repo-handoff.md §3.
"""

import json
import re
import shlex
import sys


# Targets that, when paired with rm -rf, indicate a catastrophic action.
DANGEROUS_RM_TARGETS = {
    "/", "/*", "~", "~/*", "*", ".", "..", "$HOME",
    "/usr", "/etc", "/var", "/bin", "/sbin", "/opt", "/root",
    "/lib", "/boot", "/Users", "/home",
    "C:", "C:\\", "C:/", "C:\\*", "C:/*",
}


def parse_command(command):
    """Tokenize the command. Return None on parse error (fail open)."""
    try:
        return shlex.split(command, posix=True)
    except ValueError:
        return None


def check_rm_rf(tokens):
    """Block rm with -r and -f flags when targeting dangerous paths."""
    if not tokens or tokens[0] != "rm":
        return None

    has_recursive = False
    has_force = False
    targets = []

    for tok in tokens[1:]:
        if tok in ("--recursive", "--no-preserve-root"):
            has_recursive = True
        elif tok == "--force":
            has_force = True
        elif tok.startswith("--"):
            continue
        elif tok.startswith("-") and len(tok) >= 2:
            for c in tok[1:]:
                if c in ("r", "R"):
                    has_recursive = True
                elif c == "f":
                    has_force = True
        else:
            targets.append(tok)

    if not (has_recursive and has_force):
        return None

    for target in targets:
        if target in DANGEROUS_RM_TARGETS:
            return f"rm -rf on dangerous target: {target!r}"
        if target.startswith("$HOME") or target == "~" or target.startswith("~/"):
            return f"rm -rf on home directory: {target!r}"
        # Single-segment absolute paths like /usr, /etc are suspicious.
        if target.startswith("/") and target.count("/") <= 2 and len(target) <= 8:
            return f"rm -rf on system-level path: {target!r}"

    return None


def check_static_patterns(command):
    """Regex-only checks that do not need tokenization."""
    patterns = [
        (
            r"\bgit\s+push\s+(?!.*--force-with-lease).*?(--force\b|-f\b)",
            "git push --force without --force-with-lease",
        ),
        (
            r"\bgit\s+reset\s+--hard\b",
            "git reset --hard",
        ),
        (
            r"\bformat\s+[A-Za-z]:",
            "Windows disk format",
        ),
        (
            r"\bdel\s+(?:/[a-zA-Z]\s+)*?/[fF].*?/[sS]"
            r"|\bdel\s+(?:/[a-zA-Z]\s+)*?/[sS].*?/[fF]",
            "Windows del /f /s",
        ),
        (
            r"\brd\s+(?:/[a-zA-Z]\s+)*?/[sS].*?/[qQ]"
            r"|\brd\s+(?:/[a-zA-Z]\s+)*?/[qQ].*?/[sS]",
            "Windows rd /s /q",
        ),
        (
            r"\bdd\b[^|;&]*\bof=/dev/(?:sd|nvme|hd|disk|xvd)",
            "dd writing to a disk device",
        ),
        (
            r"\bmkfs(?:\.\w+)?\s+",
            "mkfs filesystem creation",
        ),
        (
            r"\bchmod\s+(?:-R\s+|--recursive\s+)?[0-7]*777"
            r"\s+(?:/(?:\s|$|;)|/(?:usr|etc|var|bin|sbin|opt|root)\b)",
            "chmod 777 on system path",
        ),
    ]
    for pattern, label in patterns:
        if re.search(pattern, command):
            return label
    return None


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        sys.exit(0)  # fail open on parse errors

    tool_name = payload.get("tool_name", "")
    if tool_name not in ("Bash", "PowerShell"):
        sys.exit(0)

    command = payload.get("tool_input", {}).get("command", "")
    if not command:
        sys.exit(0)

    reason = check_static_patterns(command)
    if not reason:
        tokens = parse_command(command)
        if tokens is not None:
            reason = check_rm_rf(tokens)

    if reason:
        sys.stderr.write(f"pre-bash-guard blocked: {reason}\n")
        sys.stderr.write(f"Command: {command}\n")
        sys.stderr.write(
            "If this is intentional, run it manually outside Claude Code.\n"
        )
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
