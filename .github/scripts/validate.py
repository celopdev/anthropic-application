#!/usr/bin/env python3
"""
Claude Code plugin validator.
Checks the plugin follows the spec: https://code.claude.com/docs/en/plugins-reference
"""

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Missing dependency: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent.parent / "plugins" / "celestin"
errors = []
warnings = []


def error(msg):
    errors.append(msg)
    print(f"  ✗ {msg}")


def warn(msg):
    warnings.append(msg)
    print(f"  ⚠ {msg}")


def ok(msg):
    print(f"  ✓ {msg}")


def parse_frontmatter(path):
    content = path.read_text(encoding="utf-8")
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        fm = yaml.safe_load(parts[1])
        return fm or {}, parts[2].strip()
    except yaml.YAMLError as e:
        error(f"{path.relative_to(REPO_ROOT)}: YAML parse error — {e}")
        return None, content


# ── plugin.json ───────────────────────────────────────────────────────────────
print("\n── plugin.json ──────────────────────────────────────────")

manifest_path = REPO_ROOT / ".claude-plugin" / "plugin.json"
manifest = {}

if not manifest_path.exists():
    error("Missing .claude-plugin/plugin.json")
else:
    try:
        manifest = json.loads(manifest_path.read_text())
    except json.JSONDecodeError as e:
        error(f"plugin.json: invalid JSON — {e}")

    if "name" not in manifest:
        error("plugin.json: missing required 'name' field")
    else:
        name = manifest["name"]
        if " " in name:
            error(f"plugin.json: 'name' must be kebab-case, no spaces — got '{name}'")
        else:
            ok(f"name = '{name}'")

    if "version" not in manifest:
        warn("plugin.json: no 'version' field (recommended)")
    else:
        ok(f"version = '{manifest['version']}'")

    if "description" not in manifest:
        warn("plugin.json: no 'description' field (recommended)")
    else:
        ok("description present")

    invalid_fields = {"category", "tags", "strict", "source"}
    found_invalid = invalid_fields & set(manifest.keys())
    for field in found_invalid:
        error(f"plugin.json: '{field}' is a marketplace-only field, not valid in plugin.json")


# ── marketplace.json ──────────────────────────────────────────────────────────
print("\n── marketplace.json ─────────────────────────────────────")

marketplace_path = REPO_ROOT / ".claude-plugin" / "marketplace.json"

if not marketplace_path.exists():
    warn("No marketplace.json found (optional)")
else:
    try:
        market = json.loads(marketplace_path.read_text())
    except json.JSONDecodeError as e:
        error(f"marketplace.json: invalid JSON — {e}")
        market = {}

    if "name" not in market:
        error("marketplace.json: missing required 'name' field")
    else:
        ok(f"name = '{market['name']}'")

    owner = market.get("owner", {})
    if not owner.get("name"):
        error("marketplace.json: missing required 'owner.name' field")
    else:
        ok(f"owner = '{owner['name']}'")

    plugins = market.get("plugins", [])
    if not plugins:
        warn("marketplace.json: no plugins defined")

    for i, plugin in enumerate(plugins):
        prefix = f"marketplace.json plugins[{i}]"
        if "name" not in plugin:
            error(f"{prefix}: missing required 'name' field")
        if "source" not in plugin:
            error(f"{prefix}: missing required 'source' field")

        # Warn if version set in both places — plugin.json wins silently
        if "version" in plugin and "version" in manifest:
            error(
                f"{prefix}: 'version' is set in both marketplace.json and plugin.json — "
                "plugin.json wins silently. Remove from one."
            )
        else:
            ok(f"plugin '{plugin.get('name', i)}' entry valid")


# ── skills/ ───────────────────────────────────────────────────────────────────
print("\n── skills/ ──────────────────────────────────────────────")

skills_dir = REPO_ROOT / "skills"

if not skills_dir.exists():
    warn("No skills/ directory found")
else:
    skill_dirs = [d for d in sorted(skills_dir.iterdir()) if d.is_dir()]
    if not skill_dirs:
        warn("skills/ directory is empty")

    for skill_dir in skill_dirs:
        print(f"\n  [{skill_dir.name}]")
        skill_md = skill_dir / "SKILL.md"

        if not skill_md.exists():
            error(f"skills/{skill_dir.name}: missing SKILL.md")
            continue

        fm, body = parse_frontmatter(skill_md)
        if fm is None:
            continue

        # description is strongly recommended
        if "description" not in fm:
            warn(f"skills/{skill_dir.name}: no 'description' — Claude won't know when to use this skill")
        else:
            ok("description present")

        # argument-hint must be a string (not a YAML list)
        if "argument-hint" in fm:
            if not isinstance(fm["argument-hint"], str):
                error(
                    f"skills/{skill_dir.name}: 'argument-hint' must be a string, "
                    f"got {type(fm['argument-hint']).__name__} — wrap in quotes"
                )
            else:
                ok("argument-hint is a string")

        # disable-model-invocation must be a boolean
        if "disable-model-invocation" in fm:
            if not isinstance(fm["disable-model-invocation"], bool):
                error(
                    f"skills/{skill_dir.name}: 'disable-model-invocation' must be a boolean "
                    f"(true/false), got '{fm['disable-model-invocation']}'"
                )
            else:
                ok(f"disable-model-invocation = {fm['disable-model-invocation']}")

        # context must be a known value if set
        if "context" in fm and fm["context"] not in ("fork",):
            error(f"skills/{skill_dir.name}: 'context' must be 'fork', got '{fm['context']}'")

        # body must not be empty
        if not body:
            error(f"skills/{skill_dir.name}: SKILL.md has no content after frontmatter")
        else:
            ok(f"body content present ({len(body)} chars)")


# ── agents/ ───────────────────────────────────────────────────────────────────
print("\n── agents/ ──────────────────────────────────────────────")

agents_dir = REPO_ROOT / "agents"

if not agents_dir.exists():
    warn("No agents/ directory found")
else:
    agent_files = sorted(agents_dir.glob("*.md"))
    if not agent_files:
        warn("agents/ directory is empty")

    for agent_file in agent_files:
        print(f"\n  [{agent_file.name}]")
        fm, body = parse_frontmatter(agent_file)
        if fm is None:
            continue

        if "name" not in fm:
            error(f"agents/{agent_file.name}: missing required 'name' field")
        else:
            ok(f"name = '{fm['name']}'")

        if "description" not in fm:
            error(f"agents/{agent_file.name}: missing required 'description' field")
        else:
            ok("description present")

        if not body:
            error(f"agents/{agent_file.name}: agent has no system prompt (body is empty)")
        else:
            ok(f"system prompt present ({len(body)} chars)")


# ── hooks/hooks.json ──────────────────────────────────────────────────────────
print("\n── hooks/hooks.json ─────────────────────────────────────")

hooks_path = REPO_ROOT / "hooks" / "hooks.json"

if not hooks_path.exists():
    warn("No hooks/hooks.json found (optional)")
else:
    try:
        hooks = json.loads(hooks_path.read_text())
        if "hooks" not in hooks:
            error("hooks/hooks.json: missing top-level 'hooks' object")
        else:
            ok(f"events defined: {list(hooks['hooks'].keys())}")
    except json.JSONDecodeError as e:
        error(f"hooks/hooks.json: invalid JSON — {e}")


# ── settings.json ─────────────────────────────────────────────────────────────
print("\n── settings.json ────────────────────────────────────────")

settings_path = REPO_ROOT / "settings.json"

if not settings_path.exists():
    warn("No settings.json found (optional)")
else:
    try:
        settings = json.loads(settings_path.read_text())
        if "agent" in settings:
            agent_name = settings["agent"]
            agent_file = REPO_ROOT / "agents" / f"{agent_name}.md"
            if not agent_file.exists():
                error(f"settings.json: default agent '{agent_name}' not found in agents/")
            else:
                ok(f"default agent = '{agent_name}' ✓")
    except json.JSONDecodeError as e:
        error(f"settings.json: invalid JSON — {e}")


# ── Summary ───────────────────────────────────────────────────────────────────
print("\n" + "─" * 57)

if errors:
    print(f"\n✗ {len(errors)} error(s) — plugin is invalid\n")
    sys.exit(1)
elif warnings:
    print(f"\n✓ Validation passed with {len(warnings)} warning(s)\n")
else:
    print("\n✓ Validation passed — plugin is clean\n")
