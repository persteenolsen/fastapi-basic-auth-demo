# tests/test_http_basic_auth.py

from security.auth import (
    get_password_hash,
    verify_password
)

# Testing password hashing and verification
def test_valid_password():
    password = "admin"

    hashed_password = get_password_hash(password)

    result = verify_password(password, hashed_password)

    print("Valid password test:", result)
    assert result is True


# Testing wrong password
def test_invalid_password():
    password = "admin"

    hashed_password = get_password_hash(password)

    result = verify_password("wrongpassword", hashed_password)

    print("Invalid password test:", result)
    assert result is False


# Testing that hashes are generated
def test_password_hash_created():
    password = "admin"

    hashed_password = get_password_hash(password)

    print("Generated hash:", hashed_password)

    assert hashed_password is not None
    assert hashed_password != password


if __name__ == "__main__":
    test_valid_password()
    test_invalid_password()
    test_password_hash_created()

    print("\nAll tests finished")