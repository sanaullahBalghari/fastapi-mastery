from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def home():
    return{"message":"Hello world "}


@app.get("/about")

def about():
    return{"Name":"sanaullah","course":"FastApi"}
@app.get("/contact")

def contact():
    return{"email":"sanaullah@email.com"}

@app.get("/skills")

def skills():
    return{  
        "skills": [
        "FastAPI",
        "Python"
    ]}

@app.get("/services")

def services():
    return{"services":[
        "web deve",
        "web design",
        "web hossting"
    ]}


@app.get("/profile")

def profile():
    return{
    "name": "Your Name",
    "city": "Your City",
    "education": "Your Education",
    "skills": [
        "Python",
        "HTML",
        "CSS"
    ]
}


@app.get("/student")

def student():

    return {
    "id": 1,
    "name": "Ali",
    "semester": 6,
    "cgpa": 3.45,
    "subjects": [
        "Python",
        "Database",
        "Networking"
    ]
}


@app.get("/student/{student_id}")

def get_student(student_id:int):
    return{
        student_id:student_id
    }


@app.get("/user/{name}")

def get_user(name:str):
    return{
        "name": name
    }


@app.get("/multiply/{num1}/{num2}")

def multiply (num1:int, num2:int):
    return{
        "result":num1*num2
    }
