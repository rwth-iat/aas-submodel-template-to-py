#!/usr/bin/env python3
"""Reads a correct file with submodels and produces python submodel-specific classes."""
import argparse
import pathlib

from aas_submodel_to_py import generator


def _auto_filename(aas_path: pathlib.Path) -> str:
    """Derive a .py filename from the input file stem (hyphens/spaces → underscores)."""
    stem = aas_path.stem.replace("-", "_").replace(" ", "_")
    return stem + ".py"


def main() -> None:
    """Execute the main routine."""
    parser = argparse.ArgumentParser("Reads a correct file with submodels and produces python submodel-specific classes")
    parser.add_argument("-i", "--aas_path", help="path to the file with submodel/-s (AASX, JSON or XML)", required=True)
    out_group = parser.add_mutually_exclusive_group(required=False)
    out_group.add_argument("-o", "--outpath", help="path to the output file")
    out_group.add_argument("-d", "--outdir", help="output directory; filename is derived from the input filename")
    parser.add_argument("-f", "--force", help="overwrite existing files", action="store_true")
    args = parser.parse_args()

    aas_path = pathlib.Path(args.aas_path)
    if args.outpath:
        out_path = pathlib.Path(args.outpath)
    elif args.outdir:
        out_path = pathlib.Path(args.outdir) / _auto_filename(aas_path)
    else:
        out_path = aas_path.parent / _auto_filename(aas_path)
    force = bool(args.force)

    if not aas_path.exists():
        raise FileNotFoundError("AAS file does not exist: {}".format(aas_path))

    out_path.parent.mkdir(exist_ok=True, parents=True)

    if not force and out_path.exists():
        raise FileExistsError("Output path already exists and --force was not specified: {}".format(out_path))

    codegen = generator.SubmodelCodegen()
    codegen.generate_from(input_file=aas_path, output_file=out_path)

    print("Generated python client code in: {}".format(out_path))


if __name__ == "__main__":
    main()
