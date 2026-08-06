from fastapi import FastAPI
from app.middleware.request_logger import log_requests

app = FastAPI()

# Register Middleware
app.middleware("http")(log_requests)


@app.get("/")
def home():
    print("Inside Home Route")
    return {
        "message": "Welcome to Middleware Practice"
    }


@app.get("/about")
def about():
    print("Inside About Route")
    return {
        "message": "About Page"
    }


@app.get("/contact")
def contact():
    print("Inside Contact Route")
    return {
        "message": "Contact Page"
    }