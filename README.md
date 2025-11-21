
# 🌥️ Cloud ERP Lite — FastAPI Backend

A lightweight, modular ERP backend built using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, **JWT Authentication**, and **Role-Based Access Control (RBAC)**.
Designed for scalability, multi-tenancy, and modern ERP workflows.

---

## 🚀 Features

### ✅ Authentication

* User registration
* Secure login with JWT
* Password hashing (bcrypt)
* Token validation middleware

### ✅ Role-Based Access Control (RBAC)

* Built-in roles: `admin`, `user`
* Protect routes using `require_admin`
* Admin-only user listing

### ✅ Modular Architecture

* Organized into `core`, `routes`, `models`
* Ready for multi-tenant expansion
* Clean and maintainable codebase

### 📦 Tech Stack

| Service          | Technology              |
| ---------------- | ----------------------- |
| Backend          | FastAPI                 |
| Database         | PostgreSQL              |
| ORM              | SQLAlchemy              |
| Auth             | OAuth2 + JWT            |
| Hashing          | Passlib (bcrypt)        |
| Containerization | Docker & Docker Compose |

---

## 📁 Project Structure

```
backend/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── database.py
│   │   ├── security.py
│   ├── models/
│   │   └── user.py
│   ├── routes/
│       ├── auth.py
│       ├── user.py
│       ├── organization.py
│       └── product.py
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🔑 Authentication Flow

1. **Register User** → hash & save password
2. **Login** → return JWT token
3. **Use Protected Routes** using:

```
Authorization: Bearer <access_token>
```

4. **Admin-only routes** require:

```python
require_admin(current_user)
```

---

## 📘 API Endpoints

### Auth

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| POST   | `/auth/register` | Register user     |
| POST   | `/auth/login`    | Login and get JWT |

### Users

| Method | Endpoint     | Role  | Description    |
| ------ | ------------ | ----- | -------------- |
| GET    | `/users/all` | admin | List all users |

Swagger Docs:
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧱 Database Schema (Users Table)

| Column        | Type     | Notes           |
| ------------- | -------- | --------------- |
| id            | int (PK) | Auto-increment  |
| email         | varchar  | Unique          |
| password_hash | text     | Hashed password |
| role          | varchar  | admin/user      |

---

## ▶️ Running Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Add `.env`

```
DATABASE_URL=postgresql://erp:erp@127.0.0.1:5432/erpdb
JWT_SECRET=your_secret_key
```

### 3. Start backend

```
uvicorn app.main:app --reload
```

### 4. Or start with Docker

```
docker-compose up --build
```

---

## 🧭 Roadmap

* Multi-tenancy (`organizations`, membership)
* Module-based permissions
* Inventory & Products API
* Admin dashboard API
* Audit logs

---

## 📄 License

MIT License

---
