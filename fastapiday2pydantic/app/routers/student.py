from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Student(BaseModel):
    id: int
    name: str
    age: int
    department: str


students = []


@router.post("/student")
def create_student(student: Student):
    students.append(student)
    return {
        "message": "Student Added",
        "student": student
    }


@router.get("/students")
def get_students():
    return students


@router.get("/student/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student.id == student_id:
            return student

    return {
        "message": "Student Not Found"
    }


@router.put("/student/{student_id}")
def update_student(student_id: int, updated_student: Student):

    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student

            return {
                "message": " student Updated Successfully",
                "student": updated_student
            }

    return {
        "message": "Student Not Found"
    }


@router.delete("/student/{student_id}")
def delete_student(student_id: int):

    for student in students:
        if student.id == student_id:
            students.remove(student)

            return {
                "message": "Student Deleted"
            }

    return {
        "message": "Student Not Found"
    }