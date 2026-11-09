# RepoGuide

Understand repositories, practice with code, and keep learning notes.

RepoGuide is a local, single-user learning workspace. Features are built incrementally: chat, repository Q&A, code execution, notes, retrieval-augmented generation (RAG), and MCP integration and deployment.

## Status

The FastAPI backend structure and `GET /health` endpoint are in place. Model integration, persistence, the frontend, tools, and skills are not implemented yet.

## Getting started

Requirements: uv and Python 3.12 or later.

Run from the repository root:

```bash
uv sync
uv run uvicorn backend.app:app --reload
```

`uv sync` installs dependencies from `uv.lock` and creates `.venv` if needed. You do not need to create or activate the environment manually.

The backend package lives in `src/backend/`. `uv sync` installs the project in editable mode, so the `backend.app:app` import path works without setting `PYTHONPATH`.

- [Health check](http://127.0.0.1:8000/health): returns `{"status":"ok"}`.
- [Interactive API docs](http://127.0.0.1:8000/docs).

Dependencies are declared in `pyproject.toml`, with resolved versions pinned in `uv.lock`. Use `uv add <package>` for application dependencies and `uv add --dev <package>` for development tools.

## Next milestone

Define the chat request and response schemas, then connect the controller and service to a LiteLLM adapter using OpenRouter. Start with a single request and response without streaming.

See [Architecture](docs/architecture.md) for the project structure and module responsibilities.
