
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Task
from app.schemas import TaskCreate, TaskResponse, TaskUpdate


router = APIRouter(prefix="/tasks", tags=["Tasks"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.model_dump())

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@router.get("", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return db.scalars(select(Task).order_by(Task.id)).all()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    return task


@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    changes = task_update.model_dump(exclude_unset=True)

    if changes.get("title", "not_provided") is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O título não pode ser nulo",
        )

    if changes.get("completed", "not_provided") is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="O campo completed não pode ser nulo",
        )

    for field, value in changes.items():
        setattr(task, field, value)

    db.commit()
    db.refresh(task)

    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    db.delete(task)
    db.commit()
