from fastapi import FastAPI
from app.database import engine, Base
from app.models.student import Student
from app.routers.student import router as student_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Management API",
    description="Basic CRUD API using FastAPI",
    version="1.0.0"
)

# Include Routers
app.include_router(
    student_router,
    prefix="/api/v1",
    tags=["Students"]
)


@app.get("/")
def root():
    return {
        "message": "Welcome to Student Management API"
    }