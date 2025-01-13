from pydantic import BaseModel
import json

class CarInput(BaseModel):
    make: str
    model: str = 'auto'
    year: int  = 2020

class CarOutput(CarInput):
    id:int

    def load_cars():
        with open("cars.json","r") as f:
            return  [CarOutput.parse_obj(obj) for obj in json.load(f)]
    
    def save_cars(cars):
        with open("cars.json", "w") as f:
            json.dump([car.dict() for car in cars], f, indent=4)