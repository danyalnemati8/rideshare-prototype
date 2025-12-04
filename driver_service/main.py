from fastapi import FastAPI

app = FastAPI()

drivers = {}

@app.get("/driver/register")
def register_driver(driver_id: str, name: str):
    drivers[driver_id] = {"name": name, "status": "available"}
    return {"message": "Driver registered", "driver": drivers[driver_id]}

@app.get("/driver/available")
def available_drivers():
    free = [d for d, data in drivers.items() if data["status"] == "available"]
    return {"available_drivers": free}
