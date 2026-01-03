# from passlib.context import CryptContext
from pwdlib import PasswordHash

from dotenv import load_dotenv
import os

from fastapi import HTTPException, status

# Load environment variables
load_dotenv()

ALGORITHM = os.getenv("ALGORITHM")

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
password_hash = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    # return pwd_context.verify(plain_password, hashed_password)
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    # return pwd_context.hash(password)
    return password_hash.hash(password)
