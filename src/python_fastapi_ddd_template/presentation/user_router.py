from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from ..application.user_service import UserService
from ..domain.user_entity import User
from .dependencies import get_user_service

router = APIRouter()

class CreateUserRequest(BaseModel):
    name: str
    email: str

@router.post("/users", response_model=User)
def create_user(request: CreateUserRequest, user_service: UserService = Depends(get_user_service)):
    try:
        return user_service.create_user(name=request.name, email=request.email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
