"""Release consistency checks for the nikon-np3-recipes repository.

Run from the repository root:

    py tools/check_release.py

Exit code 0 means every gate passed. Non-zero lists what must be fixed
before the release is pushed. Standard library only.
"""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NP3_SIZE = 392
NP3_MAGIC = b"NCP"
LUT_SIZE = 33
LUT_ENTRIES = LUT_SIZE ** 3

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
CRS_NS = "http://ns.adobe.com/camera-raw-settings/1.0/"

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".heic", ".dng", ".nef"}
ROOT_READMES = ("README.md", "README.zh-CN.md")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.S)


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.checks = 0

    def check(self, condition: bool, message: str) -> bool:
        self.checks += 1
        if not condition:
            self.errors.append(message)
        return condition


def strip_code(text: str) -> str:
    return FENCE_RE.sub("", text)


def links_in(path: Path) -> list[str]:
    raw = strip_code(path.read_text(encoding="utf-8"))
    found = []
    for target in LINK_RE.findall(raw):
        target = target.strip().split(" ")[0]
        if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
            continue
        target = target.split("#", 1)[0]
        if target:
            found.append(target)
    return found


def check_cube(path: Path, report: Report) -> None:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    header = [line.strip() for line in lines if line.strip() and not line.startswith("#")]

    size_lines = [line for line in header if line.startswith("LUT_3D_SIZE")]
    report.check(len(size_lines) == 1, f"{path.name}: missing or duplicated LUT_3D_SIZE")
    if size_lines:
        value = size_lines[0].split()[-1]
        report.check(value == str(LUT_SIZE), f"{path.name}: LUT_3D_SIZE is {value}, expected {LUT_SIZE}")

    report.check(any(line.startswith("DOMAIN_MIN") for line in header),
                 f"{path.name}: missing DOMAIN_MIN")
    report.check(any(line.startswith("DOMAIN_MAX") for line in header),
                 f"{path.name}: missing DOMAIN_MAX")

    entries = [line for line in header
               if not line.startswith(("LUT_3D_SIZE", "DOMAIN_MIN", "DOMAIN_MAX", "TITLE"))]
    report.check(len(entries) == LUT_ENTRIES,
                 f"{path.name}: {len(entries)} entries, expected {LUT_ENTRIES}")

    for index in (0, len(entries) // 2, len(entries) - 1):
        if index >= len(entries):
            break
        parts = entries[index].split()
        report.check(len(parts) == 3 and all(_is_float(p) for p in parts),
                     f"{path.name}: malformed entry at line {index}")


def _is_float(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


def check_xmp(path: Path, report: Report) -> None:
    try:
        tree = ET.parse(path)
    except ET.ParseError as exc:
        report.check(False, f"{path.name}: invalid XML ({exc})")
        return

    description = tree.getroot().find(f".//{{{RDF_NS}}}Description")
    if not report.check(description is not None, f"{path.name}: missing rdf:Description"):
        return
    preset_type = description.get(f"{{{CRS_NS}}}PresetType")
    report.check(preset_type == "Normal", f"{path.name}: PresetType is {preset_type!r}, expected 'Normal'")
    report.check(description.get(f"{{{CRS_NS}}}ProcessVersion") is not None,
                 f"{path.name}: missing ProcessVersion")
    report.check(description.find(f"{{{CRS_NS}}}ToneCurvePV2012") is not None,
                 f"{path.name}: missing ToneCurvePV2012")


def check_recipe_dir(folder: Path, report: Report, root_readmes: dict[str, str]) -> None:
    np3_files = sorted(p for p in folder.iterdir() if p.suffix.lower() == ".np3" and p.is_file())
    if not report.check(len(np3_files) == 1, f"{folder.name}: expected exactly one NP3 file, found {len(np3_files)}"):
        return

    np3 = np3_files[0]
    data = np3.read_bytes()
    report.check(len(data) == NP3_SIZE, f"{np3.name}: {len(data)} bytes, expected {NP3_SIZE}")
    report.check(data[:3] == NP3_MAGIC, f"{np3.name}: missing NCP marker")

    cube = folder / f"{np3.stem}_sRGB.cube"
    if report.check(cube.exists(), f"{folder.name}: missing {cube.name}"):
        check_cube(cube, report)

    xmp = folder / f"{np3.stem}_Lightroom.xmp"
    if report.check(xmp.exists(), f"{folder.name}: missing {xmp.name}"):
        check_xmp(xmp, report)

    readme = folder / "README.md"
    if report.check(readme.exists(), f"{folder.name}: missing README.md"):
        text = readme.read_text(encoding="utf-8")
        report.check(np3.name in text, f"{folder.name}/README.md: does not link {np3.name}")
        report.check(cube.name in text, f"{folder.name}/README.md: does not link {cube.name}")
        report.check(xmp.name in text, f"{folder.name}/README.md: does not link {xmp.name}")
        for link in links_in(readme):
            target = (folder / link).resolve()
            report.check(target.exists(), f"{folder.name}/README.md: broken link {link}")

    strays = [p.name for p in folder.iterdir() if p.suffix.lower() in IMAGE_SUFFIXES]
    report.check(not strays, f"{folder.name}: image files must not be published ({', '.join(strays)})")

    for name, text in root_readmes.items():
        report.check(f"{folder.name}/{np3.name}" in text,
                     f"{name}: missing link to {folder.name}/{np3.name}")
        report.check(f"{folder.name}/{cube.name}" in text,
                     f"{name}: missing link to {folder.name}/{cube.name}")
        report.check(f"{folder.name}/{xmp.name}" in text,
                     f"{name}: missing link to {folder.name}/{xmp.name}")

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    report.check(np3.name in changelog, f"CHANGELOG.md: no entry mentioning {np3.name}")


def main() -> int:
    report = Report()
    recipes = sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith("gr-"))

    report.check(bool(recipes), "no recipe folders found (expected gr-* directories)")

    root_readmes = {}
    for name in ROOT_READMES:
        path = ROOT / name
        if report.check(path.exists(), f"missing {name}"):
            root_readmes[name] = path.read_text(encoding="utf-8")
            for link in links_in(path):
                target = (ROOT / link).resolve()
                report.check(target.exists(), f"{name}: broken link {link}")

    for folder in recipes:
        check_recipe_dir(folder, report, root_readmes)

    print(f"check_release: {report.checks} checks, {len(report.errors)} error(s)")
    for error in report.errors:
        print(f"  FAIL  {error}")
    if report.errors:
        print("\nRelease gate failed. Fix the items above before pushing.")
        return 1
    print("Release gate passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
