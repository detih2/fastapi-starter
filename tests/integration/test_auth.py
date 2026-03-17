"""Integration tests for auth endpoints.

These require a running PostgreSQL database.
Run with: pytest tests/integration/ -v
"""

import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app

BASE = "http://test"


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.mark.anyio
async def test_register_and_login() -> None:
    """Full auth flow: register -> login -> access /me."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=BASE) as client:
        reg = await client.post(
            "/api/v1/auth/register",
            json={
                "email": "test@example.com",
                "password": "password123",
                "full_name": "Test User",
            },
        )
        assert reg.status_code == 201
        assert reg.json()["email"] == "test@example.com"

        login = await client.post(
            "/api/v1/auth/login",
            json={"email": "test@example.com", "password": "password123"},
        )
        assert login.status_code == 200
        tokens = login.json()
        assert "access_token" in tokens

        me = await client.get(
            "/api/v1/auth/me",
            headers={"Authorization": f"Bearer {tokens['access_token']}"},
        )
        assert me.status_code == 200
        assert me.json()["email"] == "test@example.com"


@pytest.mark.anyio
async def test_login_wrong_password() -> None:
    """Login with wrong password should return 401."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url=BASE) as client:
        resp = await client.post(
            "/api/v1/auth/login",
            json={"email": "nonexistent@example.com", "password": "wrong"},
        )
        assert resp.status_code == 401
