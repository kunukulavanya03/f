# FastAPI Backend

This is a FastAPI backend application.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Create a new database: `sqlite3 app.db`
3. Run the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Documentation

The API documentation is available at `/docs`.

## Usage

You can use the API by sending HTTP requests to the endpoints.

For example, you can create a new user by sending a `POST` request to `/api/users` with a JSON body containing the user's name and email.

## Testing

You can run the tests by executing `pytest` in the terminal.

## Docker

You can build a Docker image by executing `docker build -t fastapi-backend.` in the terminal.

You can run the Docker container by executing `docker run -p 8000:8000 fastapi-backend` in the terminal.