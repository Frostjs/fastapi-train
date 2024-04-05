from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",  # Префикс для всех ручек
    tags=["Tasks"],  # Тег для документации
)


# Тут содаем ручки

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],  # Так мы в документации создаем поля для ввода с привязкой к типу
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


# Декоратор app.get() создает маршрут, который обрабатывает GET-запросы по пути /tasks
class Stask:
    pass


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
