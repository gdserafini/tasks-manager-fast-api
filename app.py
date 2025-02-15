from fastapi import FastAPI
from src.controller.root import router as root_router
from src.controller.user import router as user_router


app = FastAPI()


app.include_router(root_router)
app.include_router(user_router)
