#!/usr/bin/env python3
"""Regenerate all published submodels from admin-shell-io/submodel-templates."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
AAS_SUBMODEL_TO_PY_PATH = REPO_ROOT / "aas-submodel-to-py"
if str(AAS_SUBMODEL_TO_PY_PATH) not in sys.path:
    sys.path.insert(0, str(AAS_SUBMODEL_TO_PY_PATH))


def run_command(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_")
    slug = re.sub(r"_+", "_", slug)
    return slug.lower() or "submodel"


def is_version_part(part: str) -> bool:
    return re.fullmatch(r"\d+", part) is not None


# Markers in file names of variants of a template, and the suffix of their module names
VARIANT_MARKERS = (
    (re.compile(r"withOperations", re.IGNORECASE), "with_operations"),
    (re.compile(r"(?:^|[_\s])Example(?:[_\s]|$)"), "example"),
    (re.compile(r"without_?example_?values", re.IGNORECASE), "without_example_values"),
    (re.compile(r"GenericForm", re.IGNORECASE), "generic_form"),
    (re.compile(r"forAASMetamodelV(\d+)\.(\d+)", re.IGNORECASE), "metamodel_{0}_{1}"),
)


def variant_suffixes(file_stem: str) -> list[str]:
    suffixes = []
    for pattern, suffix in VARIANT_MARKERS:
        match = pattern.search(file_stem)
        if match:
            suffixes.append(suffix.format(*match.groups()))
    return suffixes


def output_file_name(template_file: Path, published_dir: Path) -> str:
    """Module name of a template file below published/<template>/[<part>/]<version>/

    e.g. "Digital Battery Passport/1_Digital Nameplate/1/0/..._forAASMetamodelV3.1.json"
    -> "digital_battery_passport_1_digital_nameplate_1_0_metamodel_3_1.py"
    """
    rel_parts = template_file.relative_to(published_dir).parts
    folders = rel_parts[1:-1]
    version_parts = [part for part in folders if is_version_part(part)]

    if not version_parts:
        stem = slugify(template_file.stem)
        parent = slugify("_".join(rel_parts[:-1]))
        return f"{parent}_{stem}.py"

    template_name = slugify(rel_parts[0])
    name_parts = [template_name]
    for part in folders:
        if not is_version_part(part):
            # e.g. "Digital Product Passport Part-1" of "Digital Product Passport" -> "part_1"
            name_parts.append(slugify(part).removeprefix(f"{template_name}_"))
    # Join version parts with underscores so module names stay importable
    # (e.g. "digital_nameplate_3_0_1" instead of "digital_nameplate_3-0-1")
    name_parts.extend(version_parts)
    name_parts.extend(variant_suffixes(template_file.stem))
    return f"{'_'.join(name_parts)}.py"


def assign_output_names(json_files: Iterable[Path], published_dir: Path) -> dict[Path, str]:
    """Assign module names to template files; names that still collide get a counter suffix"""
    names: dict[Path, str] = {}
    collisions: dict[str, int] = {}
    for json_file in json_files:
        name = output_file_name(json_file, published_dir)
        if name in collisions:
            collisions[name] += 1
            # Double underscore keeps the counter distinguishable from a
            # version part (e.g. "x_1_0__1" vs. "x_1_0_1")
            names[json_file] = name.replace(".py", f"__{collisions[name]}.py")
        else:
            collisions[name] = 0
            names[json_file] = name
    return names


def clone_templates_repo(repo_url: str, ref: str, destination: Path) -> None:
    run_command(
        [
            "git",
            "clone",
            "--depth",
            "1",
            "--branch",
            ref,
            "--filter=blob:none",
            "--sparse",
            repo_url,
            str(destination),
        ]
    )
    run_command(["git", "sparse-checkout", "set", "published"], cwd=destination)


def load_skip_list() -> frozenset[str]:
    raw = os.environ.get("SKIP_SUBMODELS", "")
    return frozenset(line.strip() for line in raw.splitlines() if line.strip())


def regenerate_submodels(
    templates_repo: str,
    templates_ref: str,
    output_dir: Path,
    log_file: Path,
    fail_on_errors: bool,
) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)
    from aas_submodel_to_py.generator import NoSubmodelError, SubmodelCodegen

    codegen = SubmodelCodegen()
    failures: list[tuple[Path, Exception]] = []

    skip_list = load_skip_list()

    with tempfile.TemporaryDirectory(prefix="submodel-templates-") as temp_dir:
        temp_path = Path(temp_dir)
        templates_dir = temp_path / "submodel-templates"
        clone_templates_repo(templates_repo, templates_ref, templates_dir)

        published_dir = templates_dir / "published"
        json_files = sorted(published_dir.rglob("*.json"))
        staged_output_dir = temp_path / "generated"
        staged_output_dir.mkdir(parents=True, exist_ok=True)

        templates: list[Path] = []
        for json_file in json_files:
            rel_path = str(json_file.relative_to(published_dir))
            if rel_path in skip_list:
                print(f"[SKIP] {rel_path}")
            else:
                templates.append(json_file)

        for json_file, output_name in assign_output_names(templates, published_dir).items():
            output_file = staged_output_dir / output_name

            try:
                codegen.generate_from(input_file=json_file, output_file=output_file)
                print(f"[OK] {json_file.relative_to(published_dir)} -> {output_file.name}")
            except NoSubmodelError:
                # e.g. files containing only concept descriptions or a generic form
                print(f"[SKIP] {json_file.relative_to(published_dir)}: no submodel")
            except Exception as ex:  # noqa: BLE001
                failures.append((json_file, ex))
                print(f"[FAIL] {json_file.relative_to(published_dir)}: {ex}")

        for py_file in output_dir.glob("*.py"):
            if py_file.name != "__init__.py":
                py_file.unlink()

        for py_file in staged_output_dir.glob("*.py"):
            shutil.copy2(py_file, output_dir / py_file.name)

    log_file.parent.mkdir(parents=True, exist_ok=True)
    if failures:
        lines = [
            "Generation failures:",
            *[f"- {file.relative_to(published_dir)}: {err}" for file, err in failures],
            "",
        ]
        log_file.write_text("\n".join(lines), encoding="utf-8")
    elif log_file.exists():
        log_file.unlink()

    if failures and fail_on_errors:
        return 1

    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--templates-repo",
        default="https://github.com/admin-shell-io/submodel-templates.git",
        help="Git URL of the templates repository.",
    )
    parser.add_argument(
        "--templates-ref",
        default="main",
        help="Git ref (branch/tag) from the templates repository.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "py-aas-submodels" / "py_aas_submodels",
        help="Directory where generated Python files are written.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=REPO_ROOT / "py-aas-submodels" / "generation_failures.log",
        help="Path to write generation failures.",
    )
    parser.add_argument(
        "--fail-on-errors",
        action="store_true",
        help="Exit with non-zero code if one or more submodels fail to generate.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    return regenerate_submodels(
        templates_repo=args.templates_repo,
        templates_ref=args.templates_ref,
        output_dir=args.output_dir,
        log_file=args.log_file,
        fail_on_errors=args.fail_on_errors,
    )


if __name__ == "__main__":
    raise SystemExit(main())
