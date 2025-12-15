Perfect! มาสร้าง README สวยๆ กัน 🎨

สร้างไฟล์ README.md ในโปรเจค:
markdown# TODO API 📝

A production-ready RESTful API for TODO management with JWT authentication, built with FastAPI and PostgreSQL.

## ✨ Features

- 🔐 **JWT Authentication** - Secure user registration and login
- ✅ **CRUD Operations** - Create, Read, Update, Delete TODOs
- 🔍 **Filtering** - Filter by completion status
- 📄 **Pagination** - Efficient data retrieval with skip/limit
- 🔄 **Toggle Status** - Quick completion toggle
- 🏗️ **Netflix-Style Architecture** - Scalable module-based structure
- 🐘 **PostgreSQL** - Robust data persistence
- 🐳 **Docker Ready** - Containerized deployment

## 🛠️ Tech Stack

- **Framework**: FastAPI 0.115.5
- **Database**: PostgreSQL 15
- **ORM**: SQLAlchemy 2.0.36
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt
- **Validation**: Pydantic 2.10.3
- **Logging**: structlog (JSON format)

## 📁 Project Structure
```
todo-api/
├── src/
│   ├── auth/              # Authentication module
│   │   ├── models.py      # User model
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── dependency.py  # Auth dependencies
│   │   └── router.py      # Auth endpoints
│   ├── todos/             # TODO module
│   │   ├── models.py      # Todo model
│   │   ├── schemas.py     # Pydantic schemas
│   │   ├── dependency.py  # Todo dependencies
│   │   └── router.py      # Todo endpoints
│   ├── core/              # Core configurations
│   │   ├── config.py      # Settings
│   │   ├── security.py    # JWT & password utils
│   │   └── logging.py     # Structured logging
│   ├── exceptions/        # Global exception handlers
│   ├── database.py        # Database connection
│   └── main.py           # Application entry point
├── tests/                 # Test suite
├── docker-compose.yml     # Docker services
├── requirements.txt       # Python dependencies
└── .env                  # Environment variables
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker & Docker Compose
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/todo-api.git
cd todo-api
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configurations
```

5. **Start PostgreSQL with Docker**
```bash
docker-compose up -d
```

6. **Run the application**
```bash
python -m src.main
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

### Interactive Docs
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints

#### Authentication
```http
POST   /api/v1/auth/register   # Register new user
POST   /api/v1/auth/login      # Login and get JWT token
```

#### TODOs (Protected)
```http
GET    /api/v1/todos                    # List all TODOs (with filters)
POST   /api/v1/todos                    # Create new TODO
GET    /api/v1/todos/{todo_id}          # Get single TODO
PUT    /api/v1/todos/{todo_id}          # Update TODO
DELETE /api/v1/todos/{todo_id}          # Delete TODO
PATCH  /api/v1/todos/{todo_id}/toggle   # Toggle completion status
```

### Query Parameters

**GET /api/v1/todos**
- `completed` (boolean, optional) - Filter by completion status
- `skip` (integer, default: 0) - Number of records to skip
- `limit` (integer, default: 100, max: 100) - Number of records to return

## 💡 Usage Examples

### Register a new user
```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

### Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=securepassword123"
```

### Create a TODO
```bash
curl -X POST "http://localhost:8000/api/v1/todos" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "due_date": "2025-12-20T10:00:00Z"
  }'
```

### Get all TODOs (filtered)
```bash
curl -X GET "http://localhost:8000/api/v1/todos?completed=false&limit=10" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

## 🗄️ Database Schema

### Users Table
```sql
id              UUID PRIMARY KEY
email           VARCHAR(255) UNIQUE NOT NULL
username        VARCHAR(50) UNIQUE NOT NULL
hashed_password VARCHAR NOT NULL
created_at      TIMESTAMP WITH TIME ZONE
updated_at      TIMESTAMP WITH TIME ZONE
```

### Todos Table
```sql
id          UUID PRIMARY KEY
title       VARCHAR(255) NOT NULL
description TEXT
completed   BOOLEAN DEFAULT FALSE
due_date    TIMESTAMP WITH TIME ZONE
owner_id    UUID REFERENCES users(id) ON DELETE CASCADE
created_at  TIMESTAMP WITH TIME ZONE
updated_at  TIMESTAMP WITH TIME ZONE
```

## 🧪 Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src tests/
```

## 🐳 Docker Deployment
```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## ⚙️ Environment Variables
```env
DATABASE_URL=postgresql://todo_user:todo_password@localhost:5432/todo_db
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DEBUG=True
```

## 🏗️ Architecture Highlights

- **Module-Based Structure**: Netflix-style organization for scalability
- **Dependency Injection**: Clean separation of concerns
- **Pydantic Validation**: Type-safe request/response handling
- **Structured Logging**: JSON logs for production monitoring
- **Global Exception Handling**: Consistent error responses
- **JWT Security**: Secure token-based authentication

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- FastAPI for the amazing framework
- SQLAlchemy for robust ORM
- The open-source community

---

⭐ If you found this project helpful, please consider giving it a star!