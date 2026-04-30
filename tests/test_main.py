# Project:   ci-test-python-app
# License:   FSL-1.1-ALv2
# Copyright: (c) 2026 HYPERI PTY LIMITED
"""Smoke tests for the ci-test-python-app entry point."""

from __future__ import annotations

import pytest

from ci_test_python_app import __version__
from ci_test_python_app.main import main


def test_version_string_is_non_empty() -> None:
    """__version__ is a non-empty string."""
    assert isinstance(__version__, str)
    assert __version__


def test_help_output(capsys: pytest.CaptureFixture[str]) -> None:
    """--help prints usage information and exits cleanly."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])
    assert exc_info.value.code == 0
    captured = capsys.readouterr()
    assert "ci-test-python-app" in captured.out
    assert "usage" in captured.out.lower()


def test_main_returns_zero_no_args(capsys: pytest.CaptureFixture[str]) -> None:
    """main() with no args boots, logs, and returns 0."""
    exit_code = main([])
    assert exit_code == 0
    captured = capsys.readouterr()
    assert __version__ in captured.out


def test_hyperi_pylib_import_resolves() -> None:
    """The hyperi-pylib dep was actually installed (not just declared)."""
    from hyperi_pylib import logger

    assert logger is not None
