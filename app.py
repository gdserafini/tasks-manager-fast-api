from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.controller.root import router as root_router
from src.controller.user import router as user_router
from src.controller.auth import router as auth_router
from src.controller.task import router as task_router
from src.service.session import test_db_connection
import sys


async def lifespan(app: FastAPI):
    try:
        test_db_connection()
    except Exception as e:
        print(e)
        sys.exit(1)
    yield


app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(root_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(task_router)
