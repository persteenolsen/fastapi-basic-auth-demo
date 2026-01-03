from fastapi import APIRouter, Body, Depends
from typing import Annotated

# Import the get_current_username and get_current_user functions from services/users.py
from services.users import get_current_username, get_current_user, get_all_users
from services.users import get_current_username_spa, do_register_user

# With the below import statement we import the User model and reference the username of a User by:
# User.username
from models.user import User

# To Avoid confusion / conflict with the names of Models we import the schemas Objects as:
# UserSchema, UserCreateSchema and TokenSchema
from schemas.user import User as UserSchema

router_auth = APIRouter()

# Note: User Registration Endpoint disabled for Production
@router_auth.post("/register", response_model=UserSchema, tags=["user"])
def register_user(new_user = Depends(do_register_user)):
    return new_user

# Public route for authenticate the SPA Vue 3 client
# 03-01-2025 - Parsing the username and password to function in the service folder
@router_auth.post("/authenticate-spa", tags=["user"])
async def read_current_username_spa( username: str = Body(...), password: str = Body(...)) -> dict: 
      return await get_current_username_spa(username, password)

# Protected route that returns the current user's information
# Validation: 401 is returned if the Credentials are invalid and 404 if user not found
@router_auth.get("/users/me", response_model=UserSchema, tags=["user"])
def read_current_user(user: Annotated[str, Depends(get_current_user)]):
    return user

# Protected route that returns a message and the current user's Username using Credentials directly
# Validation: 401 is returned if the Credentials are invalid 
@router_auth.get("/protected-route", tags=["user"])
def protected_route(username: Annotated[str, Depends(get_current_username)]):
    return {"message": f"Hello {username}, you are authorized for this protected route!"}

# Protected route that returns all Users from the Database if the Credentials are valid 
# Validation: 401 is returned if the Credentials are invalid and 404 if no users found 
@router_auth.get("/get-all-users", response_model=list[UserSchema], tags=["user"])
def get_all_users(users: Annotated[str, Depends(get_all_users)]):
    return users