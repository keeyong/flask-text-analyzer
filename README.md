# Flask Text Analyzer (Sample App)

A small Flask app for text analysis. Designed as a **review-friendly** project for Cursor/Claude Code:
- REST endpoints with simple validation
- Unit tests via pytest
- Intentional improvement areas (Unicode tokenization, error handling, performance)

## Endpoints
- `GET /health` → health check
- `POST /analyze` (JSON) → returns text stats and top-N words
  - Request JSON:
    ```json
    { "text": "Hello world", "top": 5 }
    ```
  - Response JSON:
    ```json
    {
      "charCount": 11,
      "wordCount": 2,
      "uniqueWordCount": 2,
      "topWords": [{"word":"hello","count":1},{"word":"world","count":1}],
      "sentenceCount": 1,
      "estimatedReadingTimeSec": 1,
      "palindromes": []
    }
    ```

## Quick Start

```bash
# 0) (optional) create & activate a virtual env
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 1) install deps
pip install -r requirements.txt

# 2) run
FLASK_APP=wsgi.py FLASK_ENV=development flask run
# or
python wsgi.py  # runs app on http://127.0.0.1:5000
```

## Run Tests
```bash
pytest -q
```

## What to Review / Improve
- Unicode-aware tokenization (Korean, accents, emojis). Current regex is English-heavy.
- Policy for hyphen/apostrophe ("it's", "state-of-the-art").
- Input size limit / streaming / rate limiting.
- Better error handling & response schema validation.
- Performance: top-N selection without sorting entire frequency map.
- Add OpenAPI spec (Swagger) & request/response validation (pydantic/Marshmallow).
