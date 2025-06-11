# Gemini Text Completion App

This is a simple command-line interface (CLI) tool built in Python that uses the **Gemini API (Gemini 1.5 Flash)** to generate text completions based on user prompts. It demonstrates how model parameters like `temperature`, `top_p`, and `max_output_tokens` affect the creativity, coherence, and length of the AI's responses.

## Features

- Text generation using Gemini 1.5 Flash
- Adjustable parameters for experimentation
- User-friendly and real-time prompt input
- Includes a small report evaluating different prompt styles and generation settings

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/faresyahmadi/ai-text-completion-project.git
   cd gemini-text-completion-app
   ```
Install dependencies:

```bash
pip install google-generativeai python-dotenv
```
Create a .env file and add your Gemini API key:  

GEMINI_KEY=your_api_key_here
https://ai.google.dev/gemini-api/docs?authuser=1&hl=fr  

make sure the .env file is in the same folder as your file. DON'T SHARE YOU API KEY.

## Usage
Run the script:
  ```bash
python text_completion_app.py
```
Then enter prompts directly in the terminal. Type exit to quit.

## Report
This project includes a brief report analyzing five prompt experiments, showing how parameter tuning impacts output quality in terms of coherence, creativity, and structure.
