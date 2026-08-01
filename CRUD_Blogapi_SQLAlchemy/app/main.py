from fastapi import FastAPI

from app.database import Base, engine
import app.models

from app.routers.post import router as post_router

# Create FastAPI App
app = FastAPI()

# Create Database Tables
Base.metadata.create_all(bind=engine)

# Register Routers
app.include_router(post_router)


@app.get("/")
def root():
    return {
        "message": "Blog API is running successfully"
    }