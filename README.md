Rideshare Prototype

This is a simple rideshare simulation prototype built with FastAPI. The system consists of three microservices: the rider service, the driver service, and the matching service. Each service runs independently and communicates through simple REST endpoints.

This guide explains how to run the entire prototype from start to finish.

How to Run the Prototype
Step 1 Start the Rider Service

Open a new terminal window

Install the required Python packages

pip install fastapi uvicorn


Navigate to the rider service directory

cd rideshare-prototype/rider_service


Start the service on port 8001

uvicorn main:app --reload --port 8001


Register a rider by opening your browser and entering

http://127.0.0.1:8001/rider/register?rider_id=R1&name=John


Expected response

{"message": "Rider R1 registered successfully"}

Step 2 Start the Driver Service

Open another terminal window

Navigate to the driver service directory

cd rideshare-prototype/driver_service


Start the service on port 8002

uvicorn main:app --reload --port 8002


Register a driver by opening your browser and entering

http://127.0.0.1:8002/driver/register?driver_id=D1&name=Alice


Expected response

{"message": "Driver D1 registered successfully"}

Step 3 Request a Ride

Enter this in your browser

http://127.0.0.1:8001/rider/request?rider_id=R1


Expected response

{"message": "Ride requested", "rider_id": "R1", "status": "waiting"}

Step 4 Check Available Drivers

Enter this in your browser

http://127.0.0.1:8002/driver/available


Expected response

{"available_drivers": ["D1"]}

Step 5 Start the Matching Service

Open a third terminal window

Navigate to the matching service directory

cd rideshare-prototype/matching_service


Start the service on port 8003

uvicorn main:app --reload --port 8003


Match a rider and driver by entering

http://127.0.0.1:8003/match?rider_id=R1


Expected response

{
  "message": "Match successful",
  "rider_id": "R1",
  "driver_id": "D1"
}
