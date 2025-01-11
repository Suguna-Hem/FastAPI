from fastapi import FastAPI, HTTPException

app=FastAPI()


cars = [
        {
            "id": 10,
            "make": "Toyota",
            "model": "Corolla",
            "year": 2019
        },
        {
            "id": 20,
            "make": "Honda",
            "model": "Civic",
            "year": 2018
        },
        {
            "id": 30,
            "make": "Ford",
            "model": "Fusion",
            "year": 2017
        }
    ]

@app.get("/app/cars")
def get_cars(): 
    return {"Car Details": cars}

@app.get("/app/cars/{car_id}")
def get_carid(car_id: int):
    result = [car for car in cars if car["id"] == int(car_id)]
    if result:
        return {"Car id Details": result}
    else:
        raise HTTPException(status_code=404, detail="Car ID not found")
    
    
@app.get("/app/cars_filter")
def get_car_filter(make: str = None, year:int = None):
    result= cars
    if make and year:
        result= [car for car in cars if car["make"] == make and car["year"] == int(year)]   
    else:    
        if make:
            result= [car for car in cars if car["make"] == make]
        if year:
            result= [car for car in cars if car["year"] == int(year)]

    if result:
            return {"Car Make Details": result}
    else:
            raise HTTPException(status_code=404, detail="Car details is not found")