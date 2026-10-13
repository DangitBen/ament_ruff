#!/usr/bin/env python3

# Copyright 2025 Southwest Research Institute® (SwRI®)
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#
#    * Neither the name of the Southwest Research Institute® (SwRI®) nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
import os
import pathlib
import subprocess
import sys


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(
        description="Check or format python code using ruff",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=[pathlib.Path(os.curdir)],
        help="The files or directories to check",
        type=pathlib.Path,
    )
    parser.add_argument(
        "--config",
        metavar="path",
        default=os.path.join(os.path.dirname(__file__), "configuration", "ty.toml"),
        dest="config_file",
        help="The path to a pyproject.toml or ruff.toml config file.",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply any possible automatic fixes",
    )
    parser.add_argument(
        "--xunit-file",
        help="Generate a xunit compliant XML file",
    )
    parser.add_argument("--verbose", action="store_true", help="")

    args = parser.parse_args(argv)
    if args.config_file is not None and not os.path.exists(args.config_file):
        print(f"Could not find the config file {args.config_file}", file=sys.stderr)
        return 1

    ty_argv = []
    if args.config_file is not None:
        ty_argv.extend(["--config-file", args.config_file])

    if args.fix:
        ty_argv.append("--fix")

    if args.verbose:
        ty_argv.append("-vv")

    ty_argv.append("--")
    ty_argv.extend(args.paths)

    out_check = subprocess.run(
        ["ty", "check", "--color", "always", *ty_argv],
        capture_output=True,
        text=True,
    )

    if args.verbose:
        print(out_check.stderr)

    print(out_check.stdout)

    if args.xunit_file:
        out_check_junit = subprocess.run(
            ["ty", "check", "--output-format", "junit", *ty_argv],
            capture_output=True,
            text=True,
        )
        if args.verbose:
            print(f"Writing xunit file to: {args.xunit_file}")
        with open(args.xunit_file, "w") as f:
            f.write(out_check_junit.stdout)
    return 0


if __name__ == "__main__":
    exit(main())
