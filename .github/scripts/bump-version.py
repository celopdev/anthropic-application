#!/usr/bin/env python3
import json
import sys
from pathlib import Path

MARKETPLACE_JSON = Path(__file__).parent.parent.parent / ".claude-plugin" / "marketplace.json"

data = json.loads(MARKETPLACE_JSON.read_text())
plugin = next(p for p in data["plugins"] if p["name"] == "celestin")

major, minor, patch = map(int, plugin["version"].split("."))
bump = sys.argv[1]

if bump == "major":
    major += 1; minor = 0; patch = 0
elif bump == "minor":
    minor += 1; patch = 0
elif bump == "patch":
    patch += 1

old = plugin["version"]
plugin["version"] = f"{major}.{minor}.{patch}"

MARKETPLACE_JSON.write_text(json.dumps(data, indent=2) + "\n")
print(f"Bumped {old} → {plugin['version']} ({bump})")
