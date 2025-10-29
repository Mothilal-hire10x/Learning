# King of Codes — Learning Log

A playful, creative file to record daily learning and show something new on the streak.

This file is intentionally safe: it does NOT contain any secret API keys. If you want to call Gemini (or another LLM), set your API key in an environment variable locally and never commit it.

## Today's creative code (October 30, 2025)

A short Python micro-snippet that generates tiny code poems and prints a colourful ASCII crown.

```python
#!/usr/bin/env python3
"""
King of Codes — tiny creative generator
"""
import random

POEMS = [
    "Loops singing softly, variables hum — the algorithm reigns.",
    "A function's promise: small input, big wonder.",
    "Whitespace crowns the poet coder; clarity wins the day."
]

CROWN = [
    "   _===_   ",
    "  /  |  \  ",
    " |   |   | ",
    "  \_____/  "
]

if __name__ == '__main__':
    poem = random.choice(POEMS)
    print('\n'.join(CROWN))
    print('\nKing of Codes says:\n')
    print(poem)
```

## Safe Gemini API usage example

Do NOT paste API keys into files. Use an environment variable on your machine. Example pseudocode (Python) showing how to call a Gemini-like REST API using `GEMINI_API_KEY` from env:

```python
# Example only — replace endpoint and parameters with the correct Gemini API details
import os
import requests

API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    raise SystemExit('Set GEMINI_API_KEY in your environment before running this script.')

endpoint = 'https://api.example.com/v1/generate'  # replace with real Gemini endpoint
headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

payload = {
    'prompt': 'Write a 2-line coding haiku about recursion',
    'max_tokens': 100,
}

resp = requests.post(endpoint, headers=headers, json=payload)
print(resp.status_code, resp.text)
```

How to set the API key locally (do this in your terminal, never commit the key):

```bash
# zsh / bash - set for this session
export GEMINI_API_KEY="<put-your-key-here>"

# run the example script after setting the variable
python3 example_gemini_call.py
```

## Notes

- I did NOT include the API key you pasted. I cannot store or use secrets on your behalf. If you want me to wire up a helper that reads the key from your local environment (and doesn't commit it), I can implement that.
- This file is intentionally creative and short — you can extend it with daily learning entries that the streak script will commit.

Enjoy — long live the King of Codes!
