from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('Tables cleared')
    await create_tables()
    print('Tables created')
    yield
    print('Shutting down')


# Для запуска сервера нужно выполнить команду uvicorn main:app --reload
# Создаем экземпляр класса FastAPI
app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

