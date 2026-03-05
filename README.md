LLM Dialogue Orchestration (Python)

<p align="left"> <a href="LICENSE"> <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"> </a> <img src="https://img.shields.io/badge/Python-3.14-blue.svg" alt="Python Version"> <img src="https://img.shields.io/badge/LLM-Ollama-orange.svg" alt="Ollama"> <img src="https://img.shields.io/badge/Models-llama3.2%20%7C%20deepseek--r1-green.svg" alt="Models"> <img src="https://img.shields.io/badge/Interface-CLI-lightgrey.svg" alt="CLI"> </p>

A command-line application that orchestrates structured conversations
between multiple Large Language Models (LLMs). The system allows a user
to start a discussion and observe how different models respond,
critique, and extend each other's reasoning across several rounds.

The tool supports both **discussion mode** and **debate mode**, enabling
experimentation with different reasoning styles between models such as
**llama3.2** and **deepseek-r1** running locally via **Ollama**. All
responses are streamed in real time and logged automatically for later
analysis.

------------------------------------------------------------------------

# Snapshot

-   Status: working (simple CLI prototype).
-   Language: Python
-   Framework / API: Ollama Python client
-   Key files: `llm_dialogue_orchestration.py`, `starter_questions.txt`,
    `llm-conversation.txt`
-   Models used:
    -   `llama3.2`
    -   `deepseek-r1`
-   Outputs:
    -   `llm-conversation.txt` --- full conversation log including
        timestamps and model responses.

------------------------------------------------------------------------

# What it does

-   Allows the user to initiate a question or prompt.
-   Runs **multi-round conversations between different LLMs**.
-   Lets the user choose which model responds in each round.
-   Supports two interaction modes:

### Discussion Mode

Models generate **follow-up questions** to continue the conversation
logically.

### Debate Mode

Models **argue against previous responses**, identifying weaknesses in
reasoning.

-   Streams responses from the model in real time.
-   Logs the entire conversation to a text file for later inspection.

This setup helps explore:

-   reasoning differences between models
-   argumentation styles
-   prompt chaining behavior
-   conversational continuity in LLM interactions.

------------------------------------------------------------------------

# Quick Setup (Local)

## 1. Create and activate a virtual environment

Example using Python virtual environment:

``` bash
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.venv\Scripts\activate           # Windows
```

Or using **Anaconda**:

``` bash
conda create -n genai-ass1 python=3.14.2
conda activate genai-ass1
```

------------------------------------------------------------------------

## 2. Install required Python package

``` bash
pip install ollama
```

------------------------------------------------------------------------

## 3. Install Ollama

Download and install Ollama:

https://ollama.com

Start the Ollama service:

``` bash
ollama serve
```

------------------------------------------------------------------------

## 4. Download the required models

``` bash
ollama pull llama3.2
ollama pull deepseek-r1
```

These models will then run locally and can be accessed by the
orchestration script.

------------------------------------------------------------------------

# Running the Program

Run the main script:

``` bash
python llm_dialogue_orchestration.py
```

The program will ask you to:

1.  Enter a starting question
2.  Choose the number of conversation rounds (4--12)
3.  Enable or disable **Debate Mode**
4.  Select which model responds in each round

------------------------------------------------------------------------

# File Overview

-   `llm_dialogue_orchestration.py` --- main orchestration script that
    manages the dialogue between models.
-   `starter_questions.txt` --- collection of prompts categorized into
    philosophical, scientific, and policy-related questions.
-   `llm-conversation.txt` --- automatically generated log containing
    the entire conversation with timestamps.

------------------------------------------------------------------------

# Example Interaction

Example starting question:

    A teleporter scans every atom in your body, destroys the original,
    and reconstructs an identical copy elsewhere with all your memories
    and personality. Did you travel, or did you die and get replaced?

Example dialogue snippet:

    ROUND 1
    [llama3.2]
    The original person died because the teleportation process destroys
    the body. The reconstructed copy has identical memories but is
    technically a new entity.

    ROUND 2
    [deepseek-r1]
    If the teleporter didn't destroy the original but created an
    identical copy nearby, would that mean both individuals are you?

The conversation continues for the chosen number of rounds, with each
model responding to the evolving prompt.

------------------------------------------------------------------------

# Logging and Outputs

All interactions are automatically saved to:

    llm-conversation.txt

The log includes:

-   conversation start and end timestamps
-   round numbers
-   selected model for each round
-   prompts and generated responses

This allows the conversation to be reviewed later for analysis or
comparison.

------------------------------------------------------------------------

# Prompt Sources

The project includes a small prompt dataset in:

    starter_questions.txt

These prompts are grouped into categories such as:

-   Philosophical questions
-   Technical / scientific questions
-   Controversial or policy-related questions

Users can modify or extend this file to experiment with different types
of discussions.

------------------------------------------------------------------------

# Example Conversation Log

Example log structure:

    =====Welcome to the LLM Dialogue Orchestration=====
    Timestamp Start: 2026-03-04

    ROUND 1
    [Model: llama3.2]
    Prompt: ...
    Response: ...

    ROUND 2
    [Model: deepseek-r1]
    Prompt: ...
    Response: ...

    Timestamp End: 2026-03-04

------------------------------------------------------------------------

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file
for details.
