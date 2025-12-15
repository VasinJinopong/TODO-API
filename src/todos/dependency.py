from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from src.database import get_db
from src.todos.models import Todo
from src.auth.dependency import get_current_user
from src.auth.models import User

async def valid_todo_id(
    todo_id: UUID,
    db: Session = Depends(get_db),
    current_user :User = Depends(get_current_user)
    
) -> Todo:
    """Dependency: ตรวจสอบว่า TODO Exist และเป็นจอง user"""
    
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")
    
    
    # ตรวจสอบว่าเป็นของ user หรือไม่
    if todo.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to access this todo")
    
    return todo