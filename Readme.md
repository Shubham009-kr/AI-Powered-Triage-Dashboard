# AI-Powered Support Triage Dashboard

An AI-assisted customer support dashboard that helps support agents efficiently analyze, prioritize, and review customer support requests.

The application automatically generates AI-powered summaries, categories, priorities, confidence scores, and suggested replies while allowing agents to review and manage requests through a clean React interface.

The solution supports both **Mock AI** for local development and **Mistral AI** for real-world analysis, and is fully containerized using **Docker Compose** for simple deployment.

---

# Features

## Backend

* FastAPI REST API
* SQLite database with SQLAlchemy ORM
* AI-powered message analysis using Mistral AI
* Mock AI mode for offline development
* AI provider abstraction (Factory Pattern)
* Structured AI response validation
* Review workflow with timestamps
* Environment-based configuration
* Automatic database seeding

## Frontend

* React + TypeScript
* Material UI
* Message listing with pagination
* Message details panel
* AI analysis panel
* Editable suggested reply
* Loading and error states
* Review status management

---

# Tech Stack

## Backend

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## Frontend

* React
* TypeScript
* Material UI
* Axios
* Vite

## AI

* Mistral AI
* Mock AI Provider

## DevOps

* Docker
* Docker Compose

---

# Architecture

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

---

# Project Structure

```text
candidate-test/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── prompts/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── seed.py
│   │   └── main.py
│   │
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── README.md
└── APPROACH.md
```

---

# Quick Start (Docker)

The easiest way to run the application is with Docker Compose.

Clone the repository:

```bash
git clone <repository-url>
cd candidate-test
```

Configure the backend environment:

```env
AI_MODE=mock
MISTRAL_API_KEY=your_api_key
```

Start the application:

```bash
docker compose up --build
```

Access the application:

| Service     | URL                        |
| ----------- | -------------------------- |
| Frontend    | http://localhost:5173      |
| Backend API | http://localhost:8000      |
| Swagger UI  | http://localhost:8000/docs |

Stop the application:

```bash
docker compose down
```

---

# Local Development

## Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# API Endpoints

| Method | Endpoint                 | Description                    |
| ------ | ------------------------ | ------------------------------ |
| GET    | `/messages`              | Retrieve all customer messages |
| GET    | `/messages/{id}`         | Retrieve message details       |
| POST   | `/messages/{id}/analyze` | Analyze a message using AI     |
| POST   | `/messages/{id}/review`  | Mark a message as reviewed     |

Interactive API documentation is available at:

```text
http://localhost:8000/docs
```

---

# AI Modes

## Mock Mode

```env
AI_MODE=mock
```

Uses deterministic responses without external API calls.

Recommended for development and testing.

---

## Mistral Mode

```env
AI_MODE=mistral

MISTRAL_API_KEY=your_api_key
```

Uses the Mistral API to generate real AI analysis.

---

# AI Response Format

The AI model is instructed to return structured JSON.

Example:

```json
{
  "summary": "Customer is unable to log in.",
  "category": "Authentication",
  "priority": "High",
  "confidence": 0.94,
  "suggested_reply": "Please reset your password using the Forgot Password option..."
}
```

Every response is validated before being stored or returned.

---

# Seed Data

The application automatically seeds the database with **16 realistic customer support messages** covering scenarios such as:

* Billing issues
* Login failures
* Refund requests
* Technical bugs
* Feature requests
* Security concerns
* General inquiries
* Customer complaints

---

# Error Handling

The application gracefully handles:

* Invalid message IDs
* Database failures
* Network failures
* Invalid AI responses
* AI provider errors

Loading indicators and user-friendly messages are displayed whenever possible.

---

# Design Decisions

Some notable design choices include:

* FastAPI for lightweight, high-performance APIs.
* SQLite for portability and simple deployment.
* SQLAlchemy ORM for clean data access.
* AI Provider abstraction using the Factory Pattern.
* Structured AI response validation.
* Docker Compose for reproducible development and deployment.
* Clear separation of frontend, backend, persistence, and AI layers.

The implementation intentionally avoids unnecessary complexity while remaining extensible.

---

# Assumptions

* AI responses follow the required JSON schema.
* Reviewing a message updates its review status and timestamp.
* Authentication is outside the assignment scope.
* Batch processing is not required.

---

# Future Improvements

* User authentication
* Batch message analysis
* Retry logic for AI requests
* Background workers
* Rate limiting
* Audit logging
* Unit and integration testing
* PostgreSQL support
* Additional LLM providers

---

# Environment Variables

| Variable          | Description         |
| ----------------- | ------------------- |
| `AI_MODE`         | `mock` or `mistral` |
| `MISTRAL_API_KEY` | Mistral API key     |

---

# License

This project was developed as part of a technical assessment for an AI-Powered Support Triage Dashboard.
