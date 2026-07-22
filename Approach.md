# APPROACH.md

# AI-Powered Support Triage Dashboard

## Overview

The objective of this project was to build an AI-assisted support triage dashboard that helps customer support agents efficiently analyze and review incoming support requests.

The application enables agents to:

* View customer support messages
* Analyze messages using AI
* Automatically generate summaries, categories, priorities, confidence scores, and suggested replies
* Review AI-generated analysis before responding
* Track reviewed messages

The implementation emphasizes simplicity, maintainability, and reliability while satisfying all assignment requirements without introducing unnecessary architectural complexity.

---

# Architecture

The application follows a lightweight client-server architecture.

```text
                React + TypeScript
                        │
                 Axios REST Requests
                        │
                        ▼
              FastAPI REST Backend
                        │
        ┌───────────────┴────────────────┐
        │                                │
 SQLite Database                 AI Provider Layer
        │                    ┌────────────┴────────────┐
        │                    │                         │
        │               Mock Provider          Mistral Provider
```

The frontend is responsible only for presentation and user interactions, while the backend handles business logic, data persistence, and AI integration.

---

# Backend Design

The backend is organized into modular layers with clear separation of responsibilities.

* **API Routes** expose REST endpoints.
* **Services** contain business logic.
* **Models** define the database schema.
* **Schemas** validate request and response data.
* **Database Layer** manages persistence through SQLAlchemy.
* **AI Providers** encapsulate communication with different AI implementations.
* **Factory Pattern** selects the active AI provider using configuration.

This modular structure improves readability, maintainability, and future extensibility.

---

# AI Provider Abstraction

Rather than coupling API endpoints directly to an LLM, the application introduces an AI provider abstraction.

Benefits include:

* Switching between Mock AI and Mistral AI without modifying application code.
* Easier testing.
* Cleaner separation of concerns.
* Simplified addition of future providers such as OpenAI, Claude, or Gemini.

The active provider is configured through an environment variable:

```text
AI_MODE=mock
```

or

```text
AI_MODE=mistral
```

This allows the same application code to operate in development, testing, and production environments.

---

# Prompt Engineering

Customer messages are analyzed using a structured prompt that instructs the language model to return structured JSON instead of free-form text.

Each response includes:

* Summary
* Category
* Priority
* Confidence Score
* Suggested Reply

Using structured JSON significantly simplifies parsing and reduces ambiguity.

---

# AI Response Validation

AI-generated responses are never trusted directly.

Each response is validated before being accepted by the application.

The backend verifies the presence and structure of:

* summary
* category
* priority
* confidence
* suggested_reply

Invalid or malformed AI responses are rejected and appropriate errors are returned instead of storing unreliable data.

This defensive approach improves application reliability and protects downstream components.

---

# Database Design

SQLite was selected because it satisfies the assignment requirements while keeping deployment simple.

Reasons for choosing SQLite:

* Zero external dependencies
* Lightweight and portable
* Simple local development
* Appropriate for the expected project scale

SQLAlchemy ORM is used to manage persistence through Python models rather than raw SQL.

The database stores:

* Customer messages
* Review status
* Review timestamp

---

# Frontend Design

The frontend is implemented using React and TypeScript.

The interface follows a straightforward support-agent workflow and keeps the user focused on processing customer messages efficiently.

Main interface components include:

* Message List
* Message Details
* AI Analysis Panel

Typical workflow:

1. Select a customer message.
2. Analyze it using AI.
3. Review the generated analysis.
4. Edit the suggested reply if necessary.
5. Mark the message as reviewed.

---

# User Experience

Several usability improvements were included to provide a smooth workflow.

These include:

* Loading indicators during AI analysis
* Loading indicators during review operations
* Error handling for failed requests
* Pagination for browsing messages
* Status badges indicating reviewed and pending messages
* Editable suggested replies before sending

These additions improve clarity while keeping the interface intentionally simple.

---

# Error Handling

Error handling is implemented across the application.

Handled scenarios include:

* Invalid message IDs
* AI provider failures
* Invalid AI responses
* Database exceptions
* Network request failures

The goal is graceful failure with meaningful feedback rather than unexpected application crashes.

---

# Mock AI Mode

To satisfy the assignment requirements, a dedicated Mock AI provider was implemented.

This provider simulates AI analysis without making external API requests.

Advantages include:

* Offline development
* Deterministic testing
* No API costs
* Consistent demonstrations

Developers can switch between Mock and Mistral AI using a single configuration change.

---

# Docker Support

The project is fully containerized using Docker and Docker Compose.

Separate containers are provided for:

* FastAPI backend
* React frontend

Docker Compose manages service startup, networking, environment variables, and port mapping, allowing the complete application to be started with a single command.

Containerization provides:

* Consistent development environments
* Simplified setup
* Easy deployment
* Reduced dependency issues

---

# Design Trade-offs

The solution intentionally avoids unnecessary complexity.

Features deliberately excluded include:

* Microservices
* Background workers
* Message queues
* Authentication
* Multiple databases
* Distributed caching
* Complex state management

While these technologies are valuable for larger systems, they would increase complexity without providing significant benefits for this assignment.

Instead, the focus remained on building a clean, maintainable, and reliable implementation.

---

# Bonus Features Implemented

Additional features beyond the minimum requirements include:

* SQLite database persistence
* AI confidence score
* Review status tracking
* Review timestamp
* Docker containerization
* Environment-based AI provider switching

---

# Scalability Considerations

Although intentionally lightweight, the architecture supports future enhancements such as:

* Additional AI providers
* Authentication and authorization
* Background AI processing
* Retry mechanisms
* Audit logging
* Batch message analysis
* Rate limiting
* Unit and integration testing
* Migration to PostgreSQL or another production database

The modular backend and provider abstraction make these enhancements straightforward.

---

# Conclusion

This implementation prioritizes simplicity, reliability, maintainability, and ease of deployment.

The application separates presentation, business logic, persistence, and AI integration into well-defined layers, validates AI-generated content before use, supports both mock and real AI providers, and is fully containerized using Docker.

The result is a clean, extensible, and production-inspired solution that fulfills the assignment requirements while remaining easy to understand, develop, and deploy.
