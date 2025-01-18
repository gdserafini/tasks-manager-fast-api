from fastapi import FastAPI
from src.controller.root import router as root_router


app = FastAPI()


app.include_router(root_router)
