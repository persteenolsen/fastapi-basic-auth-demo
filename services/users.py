from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
from typing import Annotated

# Import auth functions from security/auth.py
from security.auth import verify_password, get_password_hash

# Import the database session dependency
from db.database import get_db

# With the below import statement we import the User model and reference the username of a User by:
# User.username
from models.user import User

from schemas.user import UserCreate as UserCreateSchema

security = HTTPBasic()

# Note: The below to functions are placed in service/user.py for auth related functions in 
# order to separate concerns and make the code more modular
# Public route that registers a new User in the PostgreSQL Database
def do_register_user(user: UserCreateSchema, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.username == user.username).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    
    # 25-12-2025 - Added Users Name
    new_user = User(username=user.username, name=user.name, email=user.email, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

# Gets the Username of the current User from the Credentials
# Validate if the Credentials are valid
# Return the current User with the information
def get_current_username(credentials: Annotated[HTTPBasicCredentials, Depends(security)] ):
    
    print("Hello")

    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"testuser"

    is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)
    
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"admin"

    is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)

    #print( credentials.username )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

# Public route for SPA - Need to get values from Post by Request and not crdentials
# Gets the Username and Password from the SPA client
# Validate if the Credentials are valid
# Return the current User with the information
async def get_current_username_spa( u, p ):
    
    # Test - print the username and password
    # print( 'u: ' + u )
    # print( 'p: ' + p )

    current_username_bytes = u.encode("utf8")
    correct_username_bytes = b"testuser"

    is_correct_username = secrets.compare_digest(current_username_bytes, correct_username_bytes)
    
    current_password_bytes = p.encode("utf8")
    correct_password_bytes = b"admin"

    is_correct_password = secrets.compare_digest(current_password_bytes, correct_password_bytes)

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return {"username": {u}}

# Gets the Username of the current User from the Credentials
# Validate if the Credentials are valid
# Validate if the User exist in the Database
# Return the current User with the information
def get_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    
    current_username_plain = credentials.username
    print( current_username_plain )
    current_password_plain = credentials.password
    print( current_password_plain )

    # 31-12-2025 - Get the current User if exist in the Database
    user = db.query(User).filter(User.username == current_username_plain).first()
    
    # Raise an Error if the username is wrong
    if user is None:
              
         # The 404 was default !
         # raise HTTPException(status_code=404, detail="User not found")
         
         # Testing a workaround with 401...
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password !",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # 31-12-2025 - Verify Password towards the stored password hash value
    if verify_password(current_password_plain, user.hashed_password):
        print( 'The password is correct ...' )
    else:
        print( 'The password is not correct !' ) 
    
    # Raise an Error if the password is wrong
    if not ( verify_password(current_password_plain, user.hashed_password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password !",
            headers={"WWW-Authenticate": "Basic"},
        )
           
    return user

# Gets all Users from the PostgreSQL Database
# Validate if the Credentials are valid
# Validate if there are any Users in the Database
# Returning all Users from the Database
def get_all_users(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):

    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"testuser"

    is_correct_username = secrets.compare_digest( current_username_bytes, correct_username_bytes )
    
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"admin"

    is_correct_password = secrets.compare_digest( current_password_bytes, correct_password_bytes )

    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    # Get all Users from the Database
    users = db.query(User).all()

    # If no Users found raise 404 Not Found with a custom message
    if users is None:
        raise HTTPException(status_code=404, detail="No Users found")
    
    return users