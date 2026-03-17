"""Task workflows powered by reusable prompt + LLM calls."""

from __future__ import annotations

from assistant.llm_client import generate_text
from assistant.prompts import BEGINNER_EXPLAIN_PROMPT, SUMMARY_PROMPT, quiz_prompt


def summarize_notes(text: str) -> str:
    """Generate a concise summary from notes."""
    result = generate_text(SUMMARY_PROMPT, text)
    return f"Summary\n-------\n{result}"


def explain_for_beginner(text: str) -> str:
    """Generate beginner-friendly explanation of notes."""
    result = generate_text(BEGINNER_EXPLAIN_PROMPT, text)
    return f"Beginner Explanation\n--------------------\n{result}"


def generate_quiz(text: str, count: int) -> str:
    """Generate a quiz with the requested number of questions."""
    if count < 1:
        raise ValueError("Quiz question count must be at least 1.")
    result = generate_text(quiz_prompt(count), text)
    return f"Quiz ({count} Questions)\n-------------------\n{result}"
