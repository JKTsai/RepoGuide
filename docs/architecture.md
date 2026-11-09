# RepoGuide Architecture

## Modular monolith

RepoGuide starts with a single FastAPI backend and a planned React frontend. Features are separated into modules within the same application. Microservices are not needed at this stage. Code execution may later run in a separate worker that shares services and data models with the backend.

The API follows MVC-style separation of responsibilities: React provides the view, HTTP routes act as controllers, and model responsibilities are split across persistence models, business services, and repositories. Pydantic API schemas remain separate from database models.

## Directory responsibilities

Backend code lives in `src/backend/`, with automated tests under `test/`. The project is installed as an editable package through uv, keeping Python imports under the `backend` namespace.

| Path | Responsibility | Planned examples |
| --- | --- | --- |
| `src/backend/app.py` | Create the application, register routes, and manage its lifecycle | `create_app` |
| `src/backend/controllers/` | Handle HTTP input, call services, and return responses | `chat.py`, `workspaces.py` |
| `src/backend/schemas/` | Define Pydantic API request and response types | `ChatRequest`, `ChatResponse` |
| `src/backend/services/` | Implement business workflows | Chat, repository Q&A, note creation |
| `src/backend/models/` | Define persistence models | `Conversation`, `Message`, `Note`, `Run` |
| `src/backend/repositories/` | Read and write database records | Conversation storage, note queries |
| `src/backend/integrations/` | Connect to external systems | LiteLLM, Git, Docker, vector stores |
| `src/backend/core/` | Provide shared configuration and infrastructure setup | Environment variables, logging, database connections |
| `frontend/` | Provide the user interface | React chat and editor views |

Existing empty packages mark intended responsibilities. Add implementations when needed; do not introduce unused base classes or business logic.

## Request flow

```text
React → Controller → Service → Repository → SQLite
                            → Integration → External service
```

- Keep controllers small. Model provider configuration and SQL belong elsewhere.
- Services coordinate workflows without depending on HTTP request or response objects.
- Repositories handle persistence; integrations handle external systems.
- `app.py` assembles the application. Other modules must not import it, to avoid circular dependencies.
- `/health` returns directly from its controller. It does not need a service or repository.

The first chat flow will be: chat controller → chat service → LiteLLM adapter → OpenRouter. Add conversation storage and streaming after the basic request and response flow works.

## Planned AI features

- **Tool calling:** Add thin tool interfaces that reuse service methods for searching and reading files.
- **Skills:** Store teaching instructions in the project's `skills/` directory for the agent runtime to select and load. These are product features, separate from instructions for the development assistant.
- **RAG:** Keep retrieval workflows in services and embedding and vector store adapters in integrations. Store note content in the regular database.
- **Code execution:** Create jobs through the HTTP API and run them in restricted Docker environments through a worker. A `Run` record stores the code version, stdout, stderr, and exit code.
- **MCP:** Add a protocol entry point once tools are stable. Reuse existing services instead of duplicating business logic.

Create the required directories only when implementing each feature, following the layout rules in `AGENTS.md`.

## Future changes

The current layers make responsibilities easy to follow. As chat, workspaces, and notes grow, group them into feature modules while keeping controller, service, and repository responsibilities separate within each module.

Introduce interfaces and dependency injection when needed to replace external systems or isolate tests. A full Clean Architecture template is unnecessary at this stage.

Route organization follows FastAPI's [APIRouter documentation](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
