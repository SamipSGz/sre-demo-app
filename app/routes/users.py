from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter(tags=["users"])


@router.get("/users/me")
def get_current_user(request: Request):
    return {"user": request.state.user}


@router.get("/users/{user_id}")
def get_user(user_id: int, request: Request):
    return {"user_id": user_id, "requested_by": request.state.user.get("sub")}
