from fastapi import FastAPI
from pydantic import BaseModel;
from typing import List;


app = FastAPI()




class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = []


@app.get("/")
def read_root():
    return {"message": "wellcome to fast  API"}

@app.get("/teas")
def get_teas():
    return teas;

@app.post("/teas")
def create_tea(tea:Tea):
    teas.append(tea)
    return{"message":"tea added successfully"}

@app.get("/teas/{tea_id}")
def get_tea(tea_id:int, updated_tea:Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index]=updated_tea
            return {"message":"tea updated successfully"}
    return {"message":"tea not found"}



@app.delete("/teas/{tea_id}")

def delete_tea(tea_id:int):
    for index, tea in enumerate(teas):
        if tea.id ==tea_id:
            deleted=teas.pop(index)
            return {"message":"tea deleted successfully"}
    return{"message":"tea not found"}
    
    