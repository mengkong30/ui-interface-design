"""Read-only offline validation for this release; Python 3.8+, stdlib only."""
import json
import re
from pathlib import Path


def validate(root):
    required = ["SKILL.md", "VERSION", "README.md", "LICENSE", "DISCLAIMER.md",
                "CHANGELOG.md", "agents/openai.yaml", "docs/CONFIGURATION.md",
                "docs/USAGE.md", "references/visual-system.md",
                "references/figma-workflow.md", "references/watch-case.md"]
    for name in required:
        if not (root / name).is_file():
            raise ValueError("Missing file: " + name)
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid VERSION")
    skill = (root / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---", skill, re.S)
    if not front or "name: ui-interface-design" not in front.group(1):
        raise ValueError("Invalid skill frontmatter")
    if '  version: "' + version + '"' not in front.group(1):
        raise ValueError("Metadata version mismatch")
    # This checks the deliberately limited metadata format used by this package,
    # not arbitrary YAML or host compatibility.
    lines = (root / "agents/openai.yaml").read_text(encoding="utf-8").splitlines()
    if lines[0] != "interface:":
        raise ValueError("Invalid interface header")
    values = {}
    for line in lines[1:]:
        if line.strip():
            key, value = line.strip().split(": ", 1)
            values[key] = json.loads(value)
    if values.get("display_name") != "ui界面设计":
        raise ValueError("Display name mismatch")
    if "$ui-interface-design" not in values.get("default_prompt", ""):
        raise ValueError("Missing invocation identifier")
    if not 25 <= len(values.get("short_description", "")) <= 64:
        raise ValueError("Short description length out of range")
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if "[TODO:" in text:
            raise ValueError("Unfinished scaffold: " + str(path))
        for link in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"https?://|#", link):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            if root.resolve() not in target.parents or not target.is_file():
                raise ValueError("Invalid local link: " + link)
    print("PASS: required files, UTF-8, version, metadata, and local references.")
    print("No Figma connection or design-quality test was performed.")


if __name__ == "__main__":
    validate(Path(__file__).resolve().parent.parent)
