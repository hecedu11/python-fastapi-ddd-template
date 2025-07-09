# Python FastAPI DDD Template

This is a project template for creating microservices using Python, FastAPI, and a Domain-Driven Design (DDD) architecture. It provides a solid foundation for building scalable and maintainable applications with a clean separation of concerns.

## Features

- **Domain-Driven Design (DDD)**: A layered architecture (Domain, Application, Infrastructure, Presentation) to promote a clean separation of concerns.
- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **AWS DynamoDB**: A fully managed NoSQL database service that provides fast and predictable performance with seamless scalability.
- **Dependency Injection**: A simple and effective dependency injection system to manage dependencies between layers.
- **Pydantic Settings**: A library for managing application settings and secrets from environment variables.

## Project Structure

```text
.env.example
LICENSE
README.md
requirements.txt
src
└── python_fastapi_ddd_template
    ├── __init__.py
    ├── application
    │   ├── __init__.py
    │   └── user_service.py
    ├── domain
    │   ├── __init__.py
    │   ├── user_entity.py
    │   └── user_repository.py
    ├── infrastructure
    │   ├── __init__.py
    │   ├── config.py
    │   └── dynamodb_user_repository.py
    ├── main.py
    └── presentation
        ├── __init__.py
        ├── dependencies.py
        └── user_router.py
```

## Getting Started

### Prerequisites

- Python 3.12+
- An AWS account with credentials configured locally.
- Docker (for running DynamoDB locally).

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-fastapi-ddd-template.git
cd python-fastapi-ddd-template
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file by copying the example file:

```bash
cp .env.example .env
```

Update the `.env` file with your desired settings. For local development, you can leave the default values.

### 5. Run DynamoDB Locally (Optional)

For local development, you can use the official DynamoDB Docker image:

```bash
docker run -p 8000:8000 amazon/dynamodb-local
```

### 6. Create the DynamoDB Table

You will need to create the `users` table in DynamoDB. You can do this using the AWS CLI. If you are running DynamoDB locally, you will need to add the `--endpoint-url` parameter.

```bash
aws dynamodb create-table \
    --table-name users \
    --attribute-definitions \
        AttributeName=user_id,AttributeType=S \
        AttributeName=email,AttributeType=S \
    --key-schema \
        AttributeName=user_id,KeyType=HASH \
    --global-secondary-indexes '[{
        "IndexName": "email-index",
        "KeySchema": [{"AttributeName":"email","KeyType":"HASH"}],
        "Projection": {"ProjectionType":"ALL"}
    }]' \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --endpoint-url http://localhost:8000  # Remove this line for AWS
```

### 7. Run the Application

```bash
uvicorn src.python_fastapi_ddd_template.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

- **Create User**: `POST /api/v1/users`
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## How to Use

You can use a tool like `curl` or Postman to interact with the API.

### Create a User

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/users" \
-H "Content-Type: application/json" \
-d '{
  "name": "John Doe",
  "email": "john.doe@example.com"
}'
