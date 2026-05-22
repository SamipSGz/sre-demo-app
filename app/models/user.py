from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True
    role: Optional[str] = "user"
