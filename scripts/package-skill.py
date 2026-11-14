#!/usr/bin/env python3
"""Build platform-specific upload packages from the single canonical SKILL.md.

Run from any directory:
    python scripts/package-skill.py

Outputs:
    dist/travel-companion-claude.zip  (travel-companion/SKILL.md at ZIP root)
    dist/travel-companion-gemini.zip  (SKILL.md at ZIP root)
    dist/travel-companion.md          (single-file upload / prompt source)

No third-party dependencies are required.
"""
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "SKILL.md"
DIST = ROOT / "dist"
EXPECTED_NAME = "travel-companion"


def read_skill() -> str:
    if not SOURCE.is_file():
        raise SystemExit(f"Missing canonical skill: {SOURCE}")
    content = SOURCE.read_text(encoding="utf-8")
    match = re.search(r"(?ms)^---\s*\n(.*?)\n---\s*\n", content)
    if not match:
        raise SystemExit("SKILL.md is missing YAML frontmatter.")
    name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", match.group(1))
    if not name_match:
        raise SystemExit("SKILL.md frontmatter is missing a valid name.")
    if name_match.group(1) != EXPECTED_NAME:
        raise SystemExit(
            f"Expected name '{EXPECTED_NAME}', found '{name_match.group(1)}'. "
            "Keep the skill name aligned with its package folder."
        )
    return content


def write_zip(path: Path, content: str, member: str) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(member, content)


def main() -> None:
    content = read_skill()
    DIST.mkdir(parents=True, exist_ok=True)

    claude = DIST / "travel-companion-claude.zip"
    gemini = DIST / "travel-companion-gemini.zip"
    markdown = DIST / "travel-companion.md"

    write_zip(claude, content, "travel-companion/SKILL.md")
    write_zip(gemini, content, "SKILL.md")
    markdown.write_text(content, encoding="utf-8")

    print("Created:")
    print(f"  {claude.relative_to(ROOT)}")
    print(f"  {gemini.relative_to(ROOT)}")
    print(f"  {markdown.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
