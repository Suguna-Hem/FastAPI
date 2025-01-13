from fastapi import FastAPI, HTTPException
import json
from schema import CarInput, CarOutput

app=FastAPI(title="Cars API")

cars = CarOutput.load_cars()


@app.get("/app/cars")
def get_cars(): 
    return {"Car Details": cars}

@app.get("/app/cars/{car_id}")
def get_carid(car_id: int):
    result = [car for car in cars if car.id== int(car_id)]
    if result:
        return {"Car id Details": result}
    else:
        raise HTTPException(status_code=404, detail="Car ID not found")
        
@app.get("/app/cars_filter")
def get_car_filter(make: str = None, year:int = None):
    result= cars
    if make and year:
        result= [car for car in cars if car.make == make and car.year== int(year)]   
    else:    
        if make:
            result= [car for car in cars if car.make == make]
        if year:
            result= [car for car in cars if car.year == int(year)]

    if result:
            return {"Car Make Details": result}
    else:
            raise HTTPException(status_code=404, detail="Car details is not found")
    

@app.post("/app/cars",response_model=CarOutput)
def add_car(car:CarInput)-> CarOutput:
    car= CarOutput(model=car.model, make=car.make, year=car.year, id=len(cars)+1)
    cars.append(car)
    CarOutput.save_cars(cars)
    return car

@app.delete("/app/cars/{car_id}")
def delete_car(car_id:int):
    matches= [car for car in cars if car.id == car_id]
    if matches:
        car=matches[0]
        cars.remove(car)
        CarOutput.save_cars(cars)
        return {"message": "Car deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Car ID not found")
    
@app.put("/app/cars/{car_id}",response_model=CarOutput)
def update_car(car_id:int, car:CarInput)-> CarOutput:
    matches= [car for car in cars if car.id == car_id]
    if matches:
        car=matches[0]
        car.make=car.make
        car.model=car.model
        car.year=car.year
        CarOutput.save_cars(cars)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"Car ID:{car_id} not found")
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("carsapp:app", reload=True)