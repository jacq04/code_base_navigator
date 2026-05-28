# Codebase Navigator Architecture

## Goal

Codebase Navigator helps users understand an unfamiliar repository.

The system takes a repo as input, creates a high-level summary and flowchart, then lets the user choose a specialized agent for deeper understanding.

---

## High-Level Flow

```mermaid
flowchart TD
    A[User provides repo] --> B[Repo Scanner]
    B --> C[Shared RAG / Repo Navigator Layer]
    C --> D[Agent 1: Introduction Agent]
    D --> E[Summary + Flowchart + Agent Options]
    E --> F[User selects option]

    F --> G[Agent 2: Code Assistant Agent]
    F --> H[Agent 3: Setup Support Agent]
    F --> I[Agent 4: Architecture Agent]
    F --> J[Agent 5: Code Flow Agent]
    F --> K[Agent 6: Feature Agent]