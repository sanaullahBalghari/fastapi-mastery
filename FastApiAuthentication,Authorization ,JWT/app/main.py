from fastapi import FastAPI

from app.database import engine, Base
from app.models.user import User
from app.routers.auth import router

app = FastAPI(title="FastAPI Authentication")

Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def home():
    return {"message": "Authentication Project Started"}