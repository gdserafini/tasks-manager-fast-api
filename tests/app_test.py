from fastapi import FastAPI
from src.controller.root import router as root_router
from src.controller.user import router as user_router
from src.controller.auth import router as auth_router
from src.controller.task import router as task_router


app_test = FastAPI()

app_test.include_router(root_router)
app_test.include_router(user_router)
app_test.include_router(auth_router)
app_test.include_router(task_router)
