#!/usr/bin/env python3
""""Reads a correct file with submodels and produces python submodel-specific classes."""
import argparse
import pathlib

import generator


def main() -> None:
    """Execute the main routine."""
    parser = argparse.ArgumentParser("Reads a correct file with submodels and produces python submodel-specific classes")
    parser.add_argument("--aas_path", help="path to the file with submodel/-s (AASX, JSON or XML)", required=True)
    parser.add_argument("--outpath", help="path to the output file", required=True)
    parser.add_argument("--force", help="overwrite existing files", action="store_true")
    args = parser.parse_args()

    aas_path = pathlib.Path(args.aas_path)
    out_path = pathlib.Path(args.outpath)
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
