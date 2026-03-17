# Smart Study Assistant

A Python CLI tool that uses the Groq API to:
- summarize notes
- explain concepts for beginners
- generate quiz questions with answer keys

## Tech Stack
- Python
- Groq API (`groq` SDK)
- `python-dotenv` for environment management

## Setup
1. Create and activate a virtual environment.
2. Install dependencies:
   - `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and set:
   - `GROQ_API_KEY`
   - optional `GROQ_MODEL`

## Usage
Run commands from the project root.

### Summarize
`python main.py summarize --text "Your notes here"`

### Explain for beginner
`python main.py explain --text "Photosynthesis is how plants make food..."`

### Generate quiz
`python main.py quiz --text "Newton's laws..." --count 5`

### Read input from file
`python main.py summarize --file notes.txt`

### Save output to file
`python main.py explain --file notes.txt --save-output output.txt`

## Architecture
- `assistant/llm_client.py`: Reusable Groq API call logic and error handling.
- `assistant/prompts.py`: Prompt templates for each task.
- `assistant/workflows.py`: Multi-use LLM workflows (summary, beginner explain, quiz).
- `assistant/io_utils.py`: Input loading and output formatting.
- `main.py`: CLI command routing and argument parsing.

## What this project demonstrates
- Prompt engineering for multiple AI tasks
- Reusable LLM workflow design
- Robust CLI input/output handling

## Resume bullet
Built a Python-based AI study assistant using Groq API to perform text summarization, beginner-friendly concept explanation, and quiz generation through prompt engineering and reusable LLM workflows.