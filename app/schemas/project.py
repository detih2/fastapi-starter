"""Pydantic schemas for project-related requests and responses."""

from datetime import datetime

from pydantic import BaseModel, Field


class ProjectCreate(BaseModel):
    """Create project request."""

    title: str = Field(..., min_length=1, max_length=255)
    description: str | None = None
    status: str = Field("active", max_length=50)


class ProjectUpdate(BaseModel):
    """Update project request (all fields optional)."""

    title: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None
    status: str | None = Field(None, max_length=50)


class ProjectResponse(BaseModel):
    """Project data returned in API responses."""

    id: int
    title: str
    description: str | None
    status: str
    owner_id: int
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}


class ProjectListResponse(BaseModel):
    """Paginated project list response."""

    items: list[ProjectResponse]
    total: int
    page: int
    per_page: int
