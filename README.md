# FastAPI Starter

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-pytest-green?logo=pytest&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

Production-ready REST API template built with FastAPI, SQLAlchemy 2.0, and PostgreSQL. Includes JWT authentication, CRUD operations, Alembic migrations, pytest tests, and Docker deployment.

---

## Features

- **JWT Authentication** — Register, login, token refresh with secure password hashing (bcrypt)
- **CRUD API** — Full Create/Read/Update/Delete for Projects entity with pagination and filtering
- **SQLAlchemy 2.0** — Async ORM with mapped columns and type-safe queries
- **Alembic Migrations** — Database schema versioning out of the box
- **Pydantic Validation** — Request/response schemas with automatic OpenAPI docs
- **pytest Suite** — Unit and integration tests with async support
- **Docker Compose** — App + PostgreSQL + Redis, one command to run
- **Swagger UI** — Interactive API documentation at `/docs`

---

## Quick Start

### Run with Docker (recommended)

```bash
git clone https://github.com/detih2/fastapi-starter.git
cd fastapi-starter
cp .env.example .env
docker compose up -d
```

API is available at `http://localhost:8000/docs`

### Run locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start PostgreSQL and Redis (or use docker compose up db redis -d)
alembic upgrade head
uvicorn app.main:app --reload
```

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Create a new user |
| POST | `/api/v1/auth/login` | Get JWT access + refresh tokens |
| POST | `/api/v1/auth/refresh` | Refresh access token |
| GET | `/api/v1/auth/me` | Get current user profile |

### Projects (CRUD)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/projects` | List projects (paginated, filterable) |
| POST | `/api/v1/projects` | Create a project |
| GET | `/api/v1/projects/{id}` | Get project by ID |
| PUT | `/api/v1/projects/{id}` | Update a project |
| DELETE | `/api/v1/projects/{id}` | Delete a project |

### System

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc |

---

## Project Structure

```
fastapi-starter/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── core/
│   │   ├── config.py        # Pydantic settings
│   │   ├── security.py      # JWT + password hashing
│   │   └── database.py      # Async engine & session
│   ├── models/
│   │   ├── user.py          # User model
│   │   └── project.py       # Project model
│   ├── schemas/
│   │   ├── user.py          # User request/response schemas
│   │   └── project.py       # Project request/response schemas
│   ├── api/
│   │   ├── deps.py          # Dependency injection (get_db, get_current_user)
│   │   ├── auth.py          # Auth endpoints
│   │   └── projects.py      # Project CRUD endpoints
│   └── services/
│       ├── user_service.py   # User business logic
│       └── project_service.py # Project business logic
├── alembic/                  # Database migrations
├── tests/
│   ├── unit/                 # Unit tests
│   └── integration/          # Integration tests
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── alembic.ini
├── .env.example
└── README.md
```

---

## Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL async connection | `postgresql+asyncpg://...` |
| `SECRET_KEY` | JWT signing key | — |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Access token TTL | `30` |
| `REFRESH_TOKEN_EXPIRE_DAYS` | Refresh token TTL | `7` |
| `REDIS_URL` | Redis connection string | `redis://redis:6379/0` |

---

## Testing

```bash
# Run all tests
pytest -v

# Unit tests only
pytest tests/unit/ -v

# With coverage
pytest --cov=app --cov-report=term-missing
```

---

## Tech Stack

- **Python 3.11+**
- **FastAPI** — high-performance async web framework
- **SQLAlchemy 2.0** — async ORM
- **Alembic** — database migrations
- **PostgreSQL 16** — primary database
- **Redis** — caching layer
- **Pydantic v2** — data validation
- **python-jose** — JWT tokens
- **passlib + bcrypt** — password hashing
- **pytest + httpx** — async testing

---

## License

MIT
