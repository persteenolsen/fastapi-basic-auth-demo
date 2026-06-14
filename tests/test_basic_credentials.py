# tests/test_basic_credentials.py

from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials

from services.users import get_current_username

# Testing valid credentials
def test_valid_credentials():

    credentials = HTTPBasicCredentials(
        username="testuser",
        password="admin"
    )

    result = get_current_username(credentials)

    print("Valid credentials test:", result)

    assert result == "testuser"


# Testing invalid username
def test_invalid_username():

    credentials = HTTPBasicCredentials(
        username="wronguser",
        password="admin"
    )

    try:
        get_current_username(credentials)
        assert False

    except HTTPException as e:
        print("Invalid username test:", e.detail)

        assert e.status_code == 401


# Testing invalid password
def test_invalid_password():

    credentials = HTTPBasicCredentials(
        username="testuser",
        password="wrongpassword"
    )

    try:
        get_current_username(credentials)
        assert False

    except HTTPException as e:
        print("Invalid password test:", e.detail)

        assert e.status_code == 401


if __name__ == "__main__":
    test_valid_credentials()
    test_invalid_username()
    test_invalid_password()

    print("\nAll tests finished")