#!/usr/bin/env python3
"""Fail-closed validation for the ChannelSiege product-charter state."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "product" / "charter-status.json"


def fail(message: str) -> None:
    raise SystemExit(f"product-charter gate: {message}")


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value) and all(nonempty(item) for item in value)
    if isinstance(value, dict):
        return bool(value) and all(nonempty(item) for item in value.values())
    return value is not None


def main() -> None:
    data = json.loads(STATUS_PATH.read_text(encoding="utf-8"))

    if data.get("schema_version") != 1:
        fail("unsupported schema_version")
    if data.get("product") != "channelsiege":
        fail("product identity must be channelsiege")
    if data.get("linear_issue") != "DEN-1864":
        fail("charter authority must remain DEN-1864")
    if data.get("canonical_linear_project") != "github.com/channelsiege":
        fail("canonical Linear project drifted")

    current_repos = data.get("current_public_repositories")
    if current_repos != ["channelsiege/.github"]:
        fail("public repository inventory must be updated explicitly before expansion")

    required = data.get("required_for_approval")
    if not isinstance(required, list) or len(required) < 10 or len(set(required)) != len(required):
        fail("required_for_approval must be a unique, substantive field list")

    status = data.get("status")
    approved = data.get("approved_charter")
    repository_creation_allowed = data.get("repository_creation_allowed")
    implementation_promotion_allowed = data.get("implementation_promotion_allowed")

    if status == "unresolved":
        if repository_creation_allowed is not False:
            fail("unresolved charter must forbid repository creation")
        if implementation_promotion_allowed is not False:
            fail("unresolved charter must forbid implementation promotion")
        if approved is not None:
            fail("unresolved charter cannot contain an approved_charter payload")
        print("product-charter gate: unresolved and safely fail-closed")
        return

    if status != "approved":
        fail("status must be unresolved or approved")
    if repository_creation_allowed is not True:
        fail("approved charter must explicitly allow repository creation")
    if implementation_promotion_allowed is not True:
        fail("approved charter must explicitly allow implementation promotion")
    if not isinstance(approved, dict):
        fail("approved status requires an approved_charter object")

    missing = [field for field in required if not nonempty(approved.get(field))]
    if missing:
        fail("approved charter is missing: " + ", ".join(sorted(missing)))

    sources = approved.get("source_links")
    if not isinstance(sources, list) or not sources or not all(
        isinstance(link, str) and link.startswith("https://") for link in sources
    ):
        fail("approved charter requires one or more HTTPS source_links")

    print("product-charter gate: approved charter is structurally complete")


if __name__ == "__main__":
    main()
