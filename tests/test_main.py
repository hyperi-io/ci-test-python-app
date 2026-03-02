# Project:    ci-test-python-cli
# License:    FSL-1.1-ALv2
# Copyright:  (c) 2026 HYPERI PTY LIMITED

"""Tests for the ci-test-cli entry point."""

from __future__ import annotations

import pytest

from ci_test_cli import __version__
from ci_test_cli.main import build_parser, main


def test_version_string() -> None:
    """Verify __version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert __version__ == "0.0.1"


def test_help_output(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify --help prints usage information and exits cleanly."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "ci-test-cli" in captured.out
    assert "usage" in captured.out.lower()


def test_main_returns_zero(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify main() returns 0 when called with no arguments."""
    exit_code = main([])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert __version__ in captured.out
