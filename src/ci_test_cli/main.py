# Project:    ci-test-python-cli
# License:    FSL-1.1-ALv2
# Copyright:  (c) 2026 HYPERI PTY LIMITED

"""Entry point for the ci-test-cli command."""

from __future__ import annotations

import argparse
import sys

from ci_test_cli import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build and return the argument parser for the CLI."""
    parser = argparse.ArgumentParser(
        prog="ci-test-cli",
        description="Minimal CLI for testing HyperI CI pipelines.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return an exit code.

    Parameters
    ----------
    argv:
        Optional argument list. Defaults to ``sys.argv[1:]`` when *None*.

    Returns
    -------
    int
        Exit code (0 for success).
    """
    parser = build_parser()
    parser.parse_args(argv)
    print(f"ci-test-cli {__version__}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
