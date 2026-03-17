"""Tests for JWT token creation/verification and password hashing."""

from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)


class TestPasswordHashing:
    """Password hashing and verification tests."""

    def test_hash_and_verify(self) -> None:
        """Hashed password should verify against the original."""
        password = "secure_password_123"
        hashed = hash_password(password)
        assert verify_password(password, hashed)

    def test_wrong_password(self) -> None:
        """Wrong password should not verify."""
        hashed = hash_password("correct_password")
        assert not verify_password("wrong_password", hashed)

    def test_different_hashes(self) -> None:
        """Same password should produce different hashes (bcrypt salt)."""
        h1 = hash_password("password")
        h2 = hash_password("password")
        assert h1 != h2


class TestJWT:
    """JWT token creation and decoding tests."""

    def test_access_token_roundtrip(self) -> None:
        """Access token should decode to the original subject."""
        token = create_access_token("42")
        payload = decode_token(token)
        assert payload is not None
        assert payload["sub"] == "42"
        assert payload["type"] == "access"

    def test_refresh_token_roundtrip(self) -> None:
        """Refresh token should decode to the original subject."""
        token = create_refresh_token("99")
        payload = decode_token(token)
        assert payload is not None
        assert payload["sub"] == "99"
        assert payload["type"] == "refresh"

    def test_invalid_token(self) -> None:
        """Invalid token should return None."""
        assert decode_token("garbage.token.here") is None

    def test_empty_token(self) -> None:
        """Empty token should return None."""
        assert decode_token("") is None
