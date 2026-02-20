#!/usr/bin/env python3
"""Regenerate all published submodels from admin-shell-io/submodel-templates."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable


REPO_ROOT = Path(__file__).resolve().parents[1]
AAS_SUBMODEL_TO_PY_PATH = REPO_ROOT / "aas-submodel-to-py"
if str(AAS_SUBMODEL_TO_PY_PATH) not in sys.path:
    sys.path.insert(0, str(AAS_SUBMODEL_TO_PY_PATH))

from aas_submodel_to_py.generator import SubmodelCodegen  # noqa: E402


def run_command(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_")
    slug = re.sub(r"_+", "_", slug)
    return slug.lower() or "submodel"


def find_version_parts(parts: Iterable[str]) -> list[str]:
    return [part for part in parts if re.fullmatch(r"\d+", part)]


def output_file_name(template_file: Path, published_dir: Path) -> str:
    rel_parts = template_file.relative_to(published_dir).parts
    top_level_name = rel_parts[0] if rel_parts else template_file.stem
    version_parts = find_version_parts(rel_parts[1:-1])

    if version_parts:
        return f"{slugify(top_level_name)}_{'-'.join(version_parts)}.py"

    stem = slugify(template_file.stem)
    parent = slugify("_".join(rel_parts[:-1]))
    return f"{parent}_{stem}.py"


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


def regenerate_submodels(
    templates_repo: str,
    templates_ref: str,
    output_dir: Path,
    log_file: Path,
    fail_on_errors: bool,
) -> int:
    output_dir.mkdir(parents=True, exist_ok=True)

    for py_file in output_dir.glob("*.py"):
        if py_file.name != "__init__.py":
            py_file.unlink()

    codegen = SubmodelCodegen()
    failures: list[tuple[Path, Exception]] = []

    with tempfile.TemporaryDirectory(prefix="submodel-templates-") as temp_dir:
        temp_path = Path(temp_dir)
        templates_dir = temp_path / "submodel-templates"
        clone_templates_repo(templates_repo, templates_ref, templates_dir)

        published_dir = templates_dir / "published"
        json_files = sorted(published_dir.rglob("*.json"))

        name_collisions: dict[str, int] = {}
        for json_file in json_files:
            output_name = output_file_name(json_file, published_dir)
            if output_name in name_collisions:
                name_collisions[output_name] += 1
                suffix = name_collisions[output_name]
                output_name = output_name.replace(".py", f"_{suffix}.py")
            else:
                name_collisions[output_name] = 0

            output_file = output_dir / output_name

            try:
                codegen.generate_from(input_file=json_file, output_file=output_file)
                print(f"[OK] {json_file.relative_to(published_dir)} -> {output_file.name}")
            except Exception as ex:  # noqa: BLE001
                failures.append((json_file, ex))
                print(f"[FAIL] {json_file.relative_to(published_dir)}: {ex}")

    log_file.parent.mkdir(parents=True, exist_ok=True)
    if failures:
        lines = [
            "Generation failures:",
            *[f"- {file}: {err}" for file, err in failures],
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
