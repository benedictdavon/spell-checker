# Spell Checker

A small full-stack spelling-checker prototype: a FastAPI backend validates words against a local dictionary and returns edit-distance suggestions, while a React/TypeScript frontend provides a simple accessible client.

This is a prototype, not a real-time language or grammar checker. It checks alphabetic English words only; punctuation, grammar, named entities, and non-English text are outside the current scope.

## Architecture

```text
React + TypeScript (Vite) -> POST /spellcheck -> FastAPI -> Trie + Levenshtein suggestions
```

The backend uses repository-relative data paths, typed request validation, a bounded request size, and explicit local-development CORS origins. The frontend uses a Vite proxy, so the API URL is not hard-coded into the application component.

## Run locally

### Backend

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
python -m uvicorn backend.main:app --reload --port 8000
```

### Frontend

In a second terminal:

```bash
cd frontend/spell-checker-frontend
npm ci
npm run dev
```

The Vite development server proxies `/spellcheck` to `http://127.0.0.1:8000`. Set `VITE_API_PROXY` when the backend runs elsewhere. The backend health check is available at `GET /health`.

## API

```json
POST /spellcheck
{"text":"A quik example."}
```

The response contains the misspelled word occurrences and up to three suggestions. Requests are rejected if they contain unknown fields or more than 10,000 characters.

## Validation

```bash
pytest -q
python -m compileall backend
cd frontend/spell-checker-frontend && npm run lint && npm run build
```

The dictionary files are derived from the sources recorded in the original project; no remote dictionary download is required at runtime.
