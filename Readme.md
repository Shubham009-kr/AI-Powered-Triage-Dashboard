# AI-Powered Support Triage Dashboard

An AI-assisted customer support triage dashboard that automatically analyzes incoming customer messages, classifies them, prioritizes them, generates suggested replies, and allows support agents to review and manage requests through a clean web interface.

The project is designed with a simple, maintainable architecture while following the assignment requirements, including support for both real AI and mock AI modes.

---

## Features

### Backend

* FastAPI REST API
* SQLite database with SQLAlchemy ORM
* AI-powered message analysis using Mistral AI
* Mock AI mode for offline development
* AI Provider abstraction for easy model switching
* Structured JSON validation for AI responses
* Review workflow for support agents
* Error handling and validation
* Environment-based configuration

### Frontend

* React + TypeScript
* Material UI interface
* Message listing with pagination
* Message details view
* AI analysis panel
* Editable suggested reply
* Loading and error states
* Review status management

---

# Tech Stack

## Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* Python 3.12

## Frontend

* React
* TypeScript
* Material UI
* Axios
* Vite

## AI

* Mistral AI API
* Mock AI Provider

---

# Project Structure

```text
candidate-test/
│
├── backend/
│   ├── ai/
│   │   ├── providers/
│   │   ├── factory.py
│   │   └── prompts.py
│   │
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── database.py
│   ├── main.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   ├── Dockerfile
│   └── package.json
│
├── docker-compose.yml
├── README.md
└── APPROACH.md
```

---

# Getting Started

## Prerequisites

* Python 3.12+
* Node.js 22+
* npm
* Docker (optional)

---

# Backend Setup

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env` file:

```env
AI_MODE=mock

# Required only when using Mistral
MISTRAL_API_KEY=your_api_key
```

Run the backend:

```bash
uvicorn main:app --reload
```

Backend runs at:

```text
http://localhost:8000
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# Docker

Build and start both services:

```bash
docker compose up --build
```

Stop containers:

```bash
docker compose down
```

---

# API Endpoints

| Method | Endpoint                 | Description                |
| ------ | ------------------------ | -------------------------- |
| GET    | `/messages`              | Retrieve all messages      |
| GET    | `/messages/{id}`         | Retrieve message details   |
| POST   | `/messages/{id}/analyze` | Analyze a message using AI |
| POST   | `/messages/{id}/review`  | Mark a message as reviewed |

---

# AI Modes

The application supports two AI modes.

## Mock Mode

Used for development and testing.

```env
AI_MODE=mock
```

Returns deterministic responses without making external API calls.

---

## Mistral AI Mode

Uses the Mistral API for real AI analysis.

```env
AI_MODE=mistral
MISTRAL_API_KEY=your_api_key
```

---

# AI Response Format

The AI is instructed to return structured JSON containing:

```json
{
  "summary": "...",
  "category": "...",
  "priority": "...",
  "confidence": 0.95,
  "suggested_reply": "..."
}
```

Responses are validated before being accepted by the application.

---

# Seed Data

The project includes 16 realistic customer support messages covering various scenarios, including:

* Billing issues
* Login problems
* Technical bugs
* Refund requests
* Security concerns
* Feature requests
* General inquiries
* Customer complaints

---

# Error Handling

The application includes:

* API exception handling
* Invalid AI response validation
* Missing message handling
* Network error handling
* Loading indicators
* User-friendly error messages

---

# Design Decisions

* SQLite was selected for simplicity and portability.
* FastAPI provides lightweight, high-performance REST APIs.
* AI providers are abstracted behind a common interface, allowing easy replacement of the underlying model.
* Mock mode enables development without requiring external AI services.
* AI responses are validated instead of being trusted directly.
* The architecture intentionally avoids unnecessary complexity while remaining extensible.

---

# Assumptions

* AI responses follow the required JSON structure.
* Reviewing a message updates its status and review timestamp.
* Batch processing is outside the current scope.
* Authentication is intentionally omitted as it is an optional enhancement.

---

# Future Improvements

* Backend unit tests
* Frontend tests
* Batch message analysis
* Retry logic for AI requests
* Authentication
* Rate limiting
* Audit logging
* Background job processing
* Support for additional LLM providers

---

# Environment Variables

| Variable          | Description            |
| ----------------- | ---------------------- |
| `AI_MODE`         | `mock` or `mistral`    |
| `MISTRAL_API_KEY` | API key for Mistral AI |

---

# License

This project was developed as part of a technical assessment for an AI-powered Support Triage Dashboard.
