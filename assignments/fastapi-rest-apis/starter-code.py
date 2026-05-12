from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="FastAPI Todo API")


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


TODOS: list[Todo] = []


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to your FastAPI Todo API!"}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/todos")
def list_todos(completed: Optional[bool] = None) -> list[Todo]:
    if completed is None:
        return TODOS
    return [todo for todo in TODOS if todo.completed is completed]


@app.post("/todos")
def create_todo(todo: Todo) -> Todo:
    if any(existing.id == todo.id for existing in TODOS):
        raise HTTPException(status_code=400, detail="A todo with this id already exists")
    TODOS.append(todo)
    return todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int) -> dict[str, str]:
    for index, todo in enumerate(TODOS):
        if todo.id == todo_id:
            del TODOS[index]
            return {"message": f"Todo {todo_id} deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
