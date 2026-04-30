# Project:   ci-test-python-app
# License:   FSL-1.1-ALv2
# Copyright: (c) 2026 HYPERI PTY LIMITED
"""Entry point for the ci-test-python-app CLI.

Validates two parts of the hyperi-ci pipeline at once:

1. The hyperi-pylib dependency resolves at install time — the import
   on line 1 of ``main()`` would fail if pip didn't pull it through.
2. The container build path picks up the Dockerfile (custom mode),
   pushes the resulting image to GHCR, and the image's ``ENTRYPOINT``
   actually runs (the HEALTHCHECK exercises ``--version``).
"""

from __future__ import annotations

import argparse
import sys

from hyperi_pylib import logger

from ci_test_python_app import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="ci-test-python-app",
        description="Python app variant for the hyperi-ci test matrix.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run the CLI and return an exit code.

    The CLI is intentionally trivial — it only needs to prove that the
    binary boots, can resolve hyperi-pylib at runtime, and emits a
    log line. The full container build/push path is what's actually
    being validated by CI.

    Args:
        argv: Optional argument list. Defaults to ``sys.argv[1:]`` when None.

    Returns:
        Exit code (0 on success).
    """
    build_parser().parse_args(argv)
    logger.info("ci-test-python-app booted", version=__version__)
    print(f"ci-test-python-app {__version__}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
