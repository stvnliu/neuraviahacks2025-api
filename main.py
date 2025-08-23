from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# {"fname":"joe","lname":"mama","age":"69","height":"100","weight":"78"}
# type TimeSeriesBMI = {
#         fname: string,
#         lname: string,
#         age: number,
#         heightMetre: number,
#         weightKg: number,
#         timestamp: number,
#     }

class Person(BaseModel):
    fname: str
    lname: str 
    age : int
    heightMetre: float
    weightKg: float
    def __init__(self, fname, lname, age, heightMetre, weightKg):
        self.age = age
        self.fname = fname
        self.lname = lname
        self.heightMetre = heightMetre
        self.weightKg = weightKg
    def BMICalculator(self) -> float:
        bmi = (self.weightKg/(self.heightMetre)^2) 
        return bmi



app = FastAPI()

@app.get("/persons/{person_id}")
async def read_person(person_id:int):
    return {"person_id:": person_id}


# TODO
@app.post("/data")
async def post_data():
    return