---
id: 1
title: Create Todo App Constitution
stage: constitution
date_iso: 2025-12-27
surface: agent
model: Qwen
feature: todo-app
branch: main
user: PMLS
command: /sp.constitution
labels:
  - constitution
  - todo-app
  - phase1
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests: []
outcome: Completed
evaluation: Successfully created the project constitution based on provided principles
---

# Create or update project constitution

## User Input

```
Project Name:
Phase 1 – Spec-Driven Todo Console Application

Purpose:
This constitution defines the non-negotiable principles, scope boundaries, and constraints for Phase 1 of the Hackathon Todo project. All specifications and future implementations must strictly follow this document.

Core Principles:
1. Spec-Driven Development is mandatory. No code may be written without an approved specification.
2. Phase-by-phase progression is required. Only Phase 1 requirements are allowed at this stage.
3. Simplicity over complexity. The solution must remain minimal and easy to understand.
4. The specification is the single source of truth.

Phase 1 Scope:
1. The application is a single-user Todo application.
2. The application runs as a console (CLI) program.
3. Tasks are stored in memory only.
4. The application supports only basic Todo functionality.

Allowed Features:
- Add a task
- View all tasks
- Update a task
- Delete a task
- Mark a task as complete or incomplete

Prohibited Features:
- Authentication or user accounts
- Databases or persistent storage
- APIs or web interfaces
- Frontend frameworks or UI design
- AI, chatbot, automation, or cloud services
- Any feature belonging to later phases

Technology Constraints:
1. Python is the only implementation language for Phase 1.
2. No external services or infrastructure are allowed.
3. Implementation details must not appear in this constitution.

Change Management Rules:
1. Any change in scope must update this constitution first.
2. If a requirement is unclear, the agent must stop and request clarification.
3. No assumptions beyond what is written in the specifications are allowed.

Success Criteria:
Phase 1 is successful when the project rules and boundaries are clearly defined, enabling the Todo application to be specified and implemented without ambiguity.
```

## Response

I have successfully created the project constitution for the Phase 1 – Spec-Driven Todo Console Application based on your provided principles. The constitution has been written to `.specify/memory/constitution.md` with version 1.0.0.

The constitution includes:
- Core Principles: Spec-Driven Development, Phase-by-Phase Progression, Simplicity Over Complexity, Specification as Single Source of Truth, Scope Boundaries, and Technology Constraints
- Allowed and Prohibited Features sections
- Change Management Rules
- Governance section with success criteria

The constitution is now ready to guide the specification and implementation of the Phase 1 Todo Console Application.