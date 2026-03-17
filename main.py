"""CLI entrypoint for Smart Study Assistant."""

from __future__ import annotations

import argparse

from assistant.io_utils import format_output, read_input_text, save_output
from assistant.llm_client import LLMClientError
from assistant.workflows import explain_for_beginner, generate_quiz, summarize_notes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Smart Study Assistant")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_arguments(cmd_parser: argparse.ArgumentParser) -> None:
        cmd_parser.add_argument(
            "--text",
            type=str,
            help="Direct text input to process.",
        )
        cmd_parser.add_argument(
            "--file",
            type=str,
            help="Path to a text file containing notes.",
        )
        cmd_parser.add_argument(
            "--save-output",
            type=str,
            help="Optional output file path to save results.",
        )

    summarize_parser = subparsers.add_parser("summarize", help="Summarize notes.")
    add_common_arguments(summarize_parser)

    explain_parser = subparsers.add_parser("explain", help="Explain for beginners.")
    add_common_arguments(explain_parser)

    quiz_parser = subparsers.add_parser("quiz", help="Generate quiz questions.")
    add_common_arguments(quiz_parser)
    quiz_parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of quiz questions to generate (default: 5).",
    )

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        input_text = read_input_text(args.text, args.file)

        if args.command == "summarize":
            result = summarize_notes(input_text)
            title = "Smart Study Assistant - Summary"
        elif args.command == "explain":
            result = explain_for_beginner(input_text)
            title = "Smart Study Assistant - Beginner Explanation"
        else:
            result = generate_quiz(input_text, args.count)
            title = "Smart Study Assistant - Quiz"

        output = format_output(title, result)
        print(output)

        if args.save_output:
            save_output(args.save_output, output)
            print(f"Saved output to: {args.save_output}")

    except (ValueError, LLMClientError) as exc:
        print(f"Error: {exc}")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
