# 🔐 HTTP Basic Authentication API (FastAPI + PostgreSQL)

A REST API built with FastAPI that demonstrates HTTP Basic authentication for Single Page Applications (SPAs).

This project was created to learn modern backend architecture, authentication flows, database migrations, manuel tests, and deployment practices using Python.

**Last updated:**
- 14-07-2026

**Python version:**
- 3.12

---

## ✨ Features

- User registration and authentication
- HTTP Basic Authentication
- Protected routes with dependency injection
- Password hashing using pwdlib (Argon2)
- PostgreSQL integration via SQLAlchemy
- Database migrations with Alembic
- Manual authentication testing
- Swagger/OpenAPI documentation
- Modular and scalable project structure

---

## 🛠️ Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- pwdlib (Argon2)
- Uvicorn
- Python 3.12

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

Clone from GitHub:

- git clone <your-repository-url>

### 2️⃣ Create virtual environment

Using PowerShell or VS Code terminal:

- python -m venv <name_of_venv>

Activate it:

- Windows: Scripts\activate
- Mac/Linux: source bin/activate

### 3️⃣ Install dependencies

- pip install -r requirements.txt

---

## ⚙️ Environment Variables

Create a `.env` file with your configuration:

- DATABASE_URL=your_postgres_connection_string
- ALGORITHM=HS256

---

## ▶️ Run the Application

Start the FastAPI server:

- uvicorn main:app --reload

API will be available at:

- http://127.0.0.1:8000

Swagger documentation:

- http://127.0.0.1:8000/docs

---

## 🧪 Manual Tests (Authentication Verification)

This project includes lightweight manual test scripts for verifying HTTP Basic Authentication and password hashing behavior without requiring pytest.

### ▶️ Run Credential Authentication Tests

- python -m tests.test_basic_credentials

### ✅ What Is Tested

- Valid username and password authentication
- Invalid username handling
- Invalid password handling

### 📋 Example Output

Valid credentials test: testuser

Invalid username test: Incorrect username or password

Invalid password test: Incorrect username or password

All tests finished

---

## 🔑 Manual Tests (Password Hashing)

This project also includes manual tests for password hashing and verification.

### ▶️ Run Password Hash Tests

- python -m tests.test_http_basic_auth

### ✅ What Is Tested

- Password hash generation
- Valid password verification
- Invalid password verification

### 📋 Example Output

Valid password test: True

Invalid password test: False

Generated hash: $argon2id$...

All tests finished

---

## 🔒 HTTP Basic Authentication

- Authentication is handled using FastAPI's HTTPBasic security
- Passwords are hashed using Argon2 through pwdlib
- Invalid credentials return 401 Unauthorized
- Protected routes use dependency injection to validate users

---

## 🏗️ Project Structure

- db/ → Database configuration and session management
- models/ → SQLAlchemy database models
- schemas/ → Pydantic request/response schemas
- routes/user.py → User-related endpoints
- routes/simple.py → Simple/example routes
- security/ → Password hashing and authentication logic
- service/ → Business logic (e.g. current user retrieval)
- tests/ → Manual authentication verification scripts

---

## 🗄️ Database Migrations (Alembic)

Initialize Alembic:

- alembic init alembic

Create a migration:

- alembic revision --autogenerate -m "create column name"

Apply migrations:

- alembic upgrade head

---

## 🖥️ Frontend (Optional)

You can test the API using the Vue 3 client:

- https://github.com/persteenolsen/vue-fastapi-basic-auth-client

This client supports HTTP Basic Authentication and API interaction.

---

## ☁️ Deployment (Vercel)

To deploy on Vercel:

1. Configure vercel.json in your project
2. Create a new project in Vercel from your GitHub repository
3. Add environment variables from your .env file in Vercel
4. Push changes to GitHub
5. Vercel will automatically build and deploy your API

---

## 📝 Notes

- Make sure PostgreSQL is running and accessible
- Update models and run migrations when schema changes
- Use Swagger UI for quick manual testing
- Store passwords only as hashes
- Use HTTPS in production when using HTTP Basic Authentication

---

Happy coding with FastAPI 🚀