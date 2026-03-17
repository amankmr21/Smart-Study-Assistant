"""Input/output helpers for CLI workflows."""

from __future__ import annotations

from pathlib import Path


def read_input_text(text: str | None, file_path: str | None) -> str:
    """Load text from direct input or a file path."""
    if text and text.strip():
        return text.strip()

    if file_path:
        file_content = Path(file_path).read_text(encoding="utf-8").strip()
        if not file_content:
            raise ValueError("The provided file is empty.")
        return file_content

    raise ValueError("Provide input text or use --file to load notes.")


def format_output(title: str, content: str) -> str:
    """Create consistent, readable terminal output."""
    border = "=" * len(title)
    return f"{title}\n{border}\n{content.strip()}\n"


def save_output(file_path: str, content: str) -> None:
    """Save generated content to a file."""
    Path(file_path).write_text(content, encoding="utf-8")
