from fastapi import FastAPI

app = FastAPI()

riders = {}

@app.get("/rider/register")
def register_rider(rider_id: str, name: str):
    riders[rider_id] = {"name": name, "status": "idle"}
    return {"message": "Rider registered", "rider": riders[rider_id]}

@app.get("/rider/request")
def request_ride(rider_id: str):
    if rider_id not in riders:
        return {"error": "Rider not found"}

    riders[rider_id]["status"] = "waiting"
    return {"message": "Ride requested", "rider_id": rider_id}

@app.get("/rider/status")
def rider_status(rider_id: str):
    if rider_id not in riders:
        return {"error": "Rider not found"}

    return {"rider_id": rider_id, "status": riders[rider_id]["status"]}
#