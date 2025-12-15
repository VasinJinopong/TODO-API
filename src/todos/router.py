from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from src.todos import schemas
from src.todos.models import Todo
from src.todos.dependency import valid_todo_id
from src.auth.dependency import get_current_user
from src.auth.models import User
from src.database import get_db

router = APIRouter(prefix="/todos", tags=["todos"])

@router.post("/",response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo_data : schemas.TodoCreate,
    db: Session = Depends(get_db),
    current_user: User= Depends(get_current_user)
): 
    """Create new Todo"""
    new_todo = Todo(
        title= todo_data.title,
        description = todo_data.description,
        completed = todo_data.completed,
        due_date = todo_data.due_date,
        owner_id = current_user.id
    )
    
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


@router.get("/",response_model=List[schemas.TodoResponse])
async def get_todos(
    completed: Optional[bool] = Query(None, description="Filter by completed status"),
    skip: int = Query(0,ge=0),
    limit: int = Query(100,ge=1, le=100),
    db: Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    """Get all Todos for current user with filter"""
    query = db.query(Todo).filter(Todo.owner_id == current_user.id)
    
    # Filter by completed status
    if completed is not None:
        query = query.filter(Todo.completed == completed)
        
    
    # Pagination
    todos = query.offset(skip).limit(limit).all()
    
    return todos



@router.get("/{todo_id}",response_model=schemas.TodoResponse)
async def get_todo(todo: Todo = Depends(valid_todo_id)):
    """Get single TODO by ID"""
    return todo


@router.put("/{todo_id}",response_model=schemas.TodoResponse)
async def update_todo(
    todo_data: schemas.TodoUpdate,
    todo: Todo = Depends(valid_todo_id),
    db:Session = Depends(get_db)
):
    """Update TODO"""
    # Update only provided field
    if todo_data.title is not None:
        todo.title = todo_data.title
        
    if todo_data.description is not None:
        todo.description = todo_data.description
        
    if todo_data.completed is not None:
        todo.completed = todo_data.completed
        
    if todo_data.due_date is not None:
        todo.due_date = todo_data.due_date
        
    db.commit()
    db.refresh(todo)
    
    return todo


@router.delete("/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(
    todo:Todo = Depends(valid_todo_id),
    db:Session = Depends(get_db)
):
    """ DELETE TODO"""
    db.delete(todo)
    db.commit()
    
    return None


@router.patch("/{todo_id}/toggle",response_model=schemas.TodoResponse)
async def toggle_todo(
    todo: Todo = Depends(valid_todo_id),
    db: Session = Depends(get_db)
):
    """Toggle TODO Complete status"""
    todo.completed = not todo.completed
    
    db.commit()
    db.refresh(todo)
    
    return todo