from fastapi import APIRouter, Request, Query
from pydantic import BaseModel, Field
from typing import Optional

router = APIRouter(tags=["users"])


class UserQueryParams(BaseModel):
    limit: int = Field(default=10, ge=1, le=100)
    offset: int = Field(default=0, ge=0)
    role: Optional[str] = None


@router.get("/users/me")
def get_current_user(request: Request):
    return {"user": request.state.user}


@router.get("/users/{user_id}")
def get_user(user_id: int, request: Request):
    return {"user_id": user_id, "requested_by": request.state.user.get("sub")}


@router.get("/users")
def list_users(
    request: Request,
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    return {"users": [], "limit": limit, "offset": offset}
