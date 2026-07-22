# APPROACH.md

# AI-Powered Support Triage Dashboard

## Overview

The objective of this project was to build an AI-assisted support triage dashboard that enables customer support agents to efficiently manage incoming support requests.

The application allows agents to:

* View customer messages
* Analyze messages using AI
* Automatically generate summaries, categories, priorities, confidence scores, and suggested replies
* Review and manage analyzed messages

The implementation focuses on simplicity, maintainability, and reliability while satisfying the assignment requirements without introducing unnecessary architectural complexity.

---

# Architecture

The application follows a simple client-server architecture.

```text
React Frontend
        │
        │ REST API
        ▼
FastAPI Backend
        │
        ├── SQLite Database
        │
        └── AI Provider Layer
              ├── Mock Provider
              └── Mistral Provider
```

This separation keeps the frontend independent from business logic while allowing the backend to manage data persistence and AI interactions.

---

# Backend Design

The backend is organized into clear functional modules.

* **Routes** expose REST endpoints.
* **Services** contain business logic.
* **Models** define the database schema.
* **AI Providers** encapsulate interactions with different AI implementations.
* **Factory Pattern** selects the active AI provider based on configuration.

This structure keeps responsibilities separated and makes the project easier to extend and maintain.

---

# AI Provider Abstraction

Instead of directly calling the AI model from API endpoints, an abstraction layer was introduced.

Benefits include:

* Switching between Mock AI and Mistral AI without changing application code.
* Easier testing.
* Cleaner separation of concerns.
* Future support for additional LLM providers.

The active provider is selected using the environment variable:

```text
AI_MODE=mock
```

or

```text
AI_MODE=mistral
```

---

# Prompt Engineering

The AI receives a structured prompt instructing it to analyze customer messages and return structured JSON.

The expected output includes:

* Summary
* Category
* Priority
* Confidence Score
* Suggested Reply

Using structured JSON instead of free-form text simplifies parsing and reduces ambiguity.

---

# AI Response Validation

One important design decision was **not trusting AI responses directly**.

Every AI response is validated before it is accepted.

The backend verifies that the response contains:

* summary
* category
* priority
* confidence
* suggested_reply

If parsing or validation fails, an appropriate error is returned instead of storing invalid data.

This approach improves reliability and prevents malformed AI outputs from affecting the application.

---

# Database Design

SQLite was selected because:

* It satisfies assignment requirements.
* It requires no external database server.
* It simplifies local setup.
* It is sufficient for the project's scale.

SQLAlchemy ORM is used for database interaction to provide clean models and avoid raw SQL queries.

The database stores:

* Customer messages
* Review status
* Review timestamp

---

# Frontend Design

The frontend is built with React and TypeScript.

The interface is intentionally simple and focuses on the support agent workflow.

Main components include:

* Message List
* Message Details
* AI Analysis Panel

The workflow is:

1. Select a message.
2. Analyze it using AI.
3. Review the generated analysis.
4. Edit the suggested reply if needed.
5. Mark the message as reviewed.

---

# User Experience

To improve usability, the interface includes:

* Loading indicators during AI analysis
* Loading indicators during review actions
* Error messages for failed requests
* Pagination for message browsing
* Status badges for reviewed and pending messages
* Editable suggested reply before sending

These features provide clear feedback and improve the overall user experience.

---

# Error Handling

Error handling is implemented throughout the application.

Examples include:

* Invalid message IDs
* AI service failures
* Invalid AI responses
* Database errors
* Network request failures

The goal is to prevent application crashes while providing meaningful feedback to users.

---

# Mock Mode

The assignment specifically requested support for a mock AI mode.

A dedicated Mock Provider was implemented to simulate AI responses without requiring external API calls.

Benefits include:

* Offline development
* Consistent testing
* No API costs
* Reliable demonstrations

---

# Design Trade-offs

The project intentionally avoids unnecessary complexity.

Features that were intentionally not introduced include:

* Microservices
* Background workers
* Message queues
* Authentication
* Multiple databases
* Caching
* Complex state management

These additions would increase maintenance effort without significantly improving the assignment solution.

Instead, the focus remained on delivering a clean, understandable, and maintainable implementation.

---

# Bonus Features Implemented

The project includes several optional enhancements:

* Database persistence using SQLite
* AI confidence score
* Review status tracking with timestamp

Additional optional features can be added in future iterations if required.

---

# Scalability Considerations

Although intentionally simple, the architecture allows future improvements such as:

* Additional AI providers
* Authentication
* Batch message analysis
* Retry logic for AI requests
* Audit logging
* Background job processing
* Unit and integration testing
* Rate limiting

The provider abstraction and modular backend structure make these enhancements straightforward to implement.

---

# Conclusion

This implementation prioritizes simplicity, reliability, and maintainability while satisfying the core assignment requirements.

The architecture is intentionally lightweight, validates AI-generated content before use, supports both mock and real AI providers, and delivers a clean user experience without introducing unnecessary complexity.

The resulting solution demonstrates practical software engineering principles while remaining easy to understand, extend, and deploy.
