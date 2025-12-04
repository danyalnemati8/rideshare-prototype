from fastapi import FastAPI
import requests

app = FastAPI()

# Update to the new ports
RIDER_SERVICE = "http://127.0.0.1:8101"
DRIVER_SERVICE = "http://127.0.0.1:8102"

@app.get("/match")
def match_driver(rider_id: str):
    # Ask rider service for status
    rider_resp = requests.get(
        f"{RIDER_SERVICE}/rider/status",
        params={"rider_id": rider_id}
    )
    rider = rider_resp.json()

    if rider.get("status") != "waiting":
        return {"error": "Rider is not waiting or does not exist"}

    # Ask driver service for available drivers
    drivers_resp = requests.get(f"{DRIVER_SERVICE}/driver/available")
    drivers = drivers_resp.json().get("available_drivers", [])

    if not drivers:
        return {"error": "No available drivers"}

    selected_driver = drivers[0]

    return {
        "message": "Match successful",
        "rider_id": rider_id,
        "driver_id": selected_driver
    }
