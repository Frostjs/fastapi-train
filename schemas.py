from typing import Optional

from pydantic import BaseModel, ConfigDict  # Импортируем класс BaseModel из модуля pydantic для моделирования данных



# Тут описываем модели для бд

class STaskAdd(BaseModel): # Создаем класс STaskAdd, который наследуется от BaseModel
    # Описываем поля класса Task
    name: str
    description: Optional[str] = None # Optional - это значит что поле может быть пустым и есть значение по умолчанию None


# Создаем класс Task, который наследуется от класса STaskAdd
class STask(STaskAdd):
    id: int

    model_config = ConfigDict(from_attributes=True) # Создаем конфигурацию модели


class STaskId(BaseModel):
    ok: bool = True
    task_id: int