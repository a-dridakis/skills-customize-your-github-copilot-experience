# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API with FastAPI by creating endpoints for creating, reading, and deleting todo items.

## 📝 Tasks

### 🛠️ Set Up a Basic FastAPI App

#### Description
Create and run a FastAPI application with a root route and a health-check route to confirm the server is working.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app in `starter-code.py`
- Add a `GET /` endpoint that returns a welcome message
- Add a `GET /health` endpoint that returns `{"status": "ok"}`
- Run the server with Uvicorn and verify both routes in the browser or with curl


### 🛠️ Build CRUD Endpoints for Todos

#### Description
Add API endpoints that let users create and list todo items stored in memory.

#### Requirements
Completed program should:

- Create a `Todo` Pydantic model with `id`, `title`, and `completed` fields
- Add a `GET /todos` endpoint that returns all todos as a list
- Add a `POST /todos` endpoint that creates a new todo and stores it in memory
- Return appropriate JSON responses from each endpoint


### 🛠️ Add Filtering and Delete Support

#### Description
Improve your API by adding query filtering and an endpoint to delete a todo by ID.

#### Requirements
Completed program should:

- Add optional query parameter `completed` to `GET /todos` for filtering
- Add a `DELETE /todos/{todo_id}` endpoint
- Return a clear error response when the todo does not exist
- Test your endpoints with at least one sample request for each route
