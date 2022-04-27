#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

import configparser
import yaml


def repos2gitmodules(repos_file: Path, output_file: Path):
    with open(repos_file, "r") as f:
        repos = yaml.load(f, Loader=yaml.SafeLoader)

    gitmodules = configparser.ConfigParser()

    for k, v in repos["repositories"].items():
        path = f"src/{k}"
        url = v["url"]
        key = f'submodule "{path}"'

        gitmodules[key] = {
            "path": path,
            "url": url,
        }

    with open(output_file, "w") as f:
        gitmodules.write(f)


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("repos_file", type=Path)
    parser.add_argument("-o", "--output", dest="output_file", type=Path, default=None)
    ns = parser.parse_args(args)

    if not ns.output_file:
        parent_dir = ns.repos_file.absolute().parent
        ns.output_file = parent_dir / ".gitmodules"

    repos2gitmodules(ns.repos_file, ns.output_file)


if __name__ == "__main__":
    main(sys.argv[1:])


# [submodule "autoware.universe"]
# path = autoware.universe
# url = https://github.com/autowarefoundation/autoware.universe
# [submodule "tmp"]
# 	path = tmp
# 	url = https://github.com/autowarefoundation/autoware.universe
