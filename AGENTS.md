# Repository Instructions

These instructions apply to the entire repository.

## Project Purpose

RepoGuide is a single-user, local learning platform for understanding repositories, practicing with code, and retaining learning notes. Develop it incrementally, following the current milestone rather than implementing future features early.

## Learning Workflow

- Work in small, reviewable steps.
- For learning tasks, explain the goal and provide hints or a minimal scaffold.
- When the user explicitly requests implementation, complete the requested scope.
- Explain important design decisions and trade-offs.

## Project Layout

- Keep application code in `src/`.
- Keep automated tests in `test/`.
- Follow this layout for new code. Do not move existing code unless the task includes that migration.

## Python Environment and Commands

- Use `uv` to manage Python dependencies and environments.
- Use `uv add <package>` for application dependencies and `uv add --dev <package>` for development dependencies.
- Use `uv sync` to install or synchronize project dependencies.
- Use `uv run <command>` to start the application and run Python tooling within the project environment.
- Do not use standalone `pip install` or require manual virtual environment activation for project workflows.

## Before Committing

- Run `uv run pre-commit run --all-files` before every commit.
- Fix failures and rerun the checks until they pass before committing.
- If pre-commit is not configured or cannot run, report the blocker; do not skip the checks or commit anyway.

## Documentation

- Write all docstrings in English.

## Change Scope

- Limit all changes to this repository, including changes made by scripts and tools.
- Do not modify files, other repositories, or global configuration outside this repository unless the user explicitly authorizes it.
- If a task requires changes outside this repository, explain the required changes and obtain permission first.

## Architecture Boundaries

- Use a modular monolith with clear responsibilities.
- Keep HTTP request handling and response mapping in controllers.
- Keep business workflows in services, independent of HTTP request and response objects.
- Keep database access in repositories and persistence models separate from API schemas.
- Keep external service adapters, including model providers, Git, and Docker, in integrations.
- Keep application startup and dependency assembly in the application entry point.
- Consult `docs/architecture.md` when changing service boundaries. Do not introduce unused layers or abstractions.

## Change Discipline

- Keep changes focused on the requested task; avoid unrelated refactoring.
- Preserve existing user changes, including uncommitted work.
- Do not overwrite or revert unrelated changes to make a task or check pass.

## Testing

- Run checks appropriate to the changed behavior and affected components.
- Add or update meaningful tests for behavior changes when appropriate; avoid tests that merely mirror implementation details.
- Mock model-provider APIs in ordinary automated tests. Do not make paid API calls by default.
- Run live-provider integration tests only when explicitly authorized, and keep them separate from ordinary tests.
- Report checks that could not run and explain why. Never claim that unexecuted checks passed.

## Secrets

- Never hardcode or commit API keys, credentials, or other secrets in source code, fixtures, or documentation.
- Load secrets from environment variables or local ignored configuration.
- Keep `.env.example` limited to placeholder values.
- Do not expose secrets in logs, error messages, or task output.

## Completion Reports

- Summarize what changed and why.
- State which checks actually ran and their results.
- Identify remaining work, blockers, and any behavior that could not be verified.
