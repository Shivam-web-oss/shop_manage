from fastapi import APIRouter
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/register")
def register_user(user: UserCreate):
    # Here you would typically add logic to save the user to the database
    return {
        "message":"User {user.name} registered successfully!",
        "data":user
    }
