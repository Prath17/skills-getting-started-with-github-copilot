from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": [
            {"name": "Michael", "email": "michael@mergington.edu"},
            {"name": "Daniel", "email": "daniel@mergington.edu"}
        ]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": [
            {"name": "Emma", "email": "emma@mergington.edu"},
            {"name": "Sophia", "email": "sophia@mergington.edu"}
        ]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": [
            {"name": "John", "email": "john@mergington.edu"},
            {"name": "Olivia", "email": "olivia@mergington.edu"}
        ]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": [
            {"name": "Liam", "email": "liam@mergington.edu"},
            {"name": "Noah", "email": "noah@mergington.edu"}
        ]
    },
    "Basketball Team": {
        "description": "Practice basketball and participate in tournaments",
        "schedule": "Wednesdays and Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": [
            {"name": "Ethan", "email": "ethan@mergington.edu"},
            {"name": "Ava", "email": "ava@mergington.edu"}
        ]
    },
    "Art Club": {
        "description": "Explore various art techniques and create your own masterpieces",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": [
            {"name": "Isabella", "email": "isabella@mergington.edu"},
            {"name": "Mia", "email": "mia@mergington.edu"}
        ]
    },
    "Drama Club": {
        "description": "Act, direct, and produce plays and performances",
        "schedule": "Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": [
            {"name": "Charlotte", "email": "charlotte@mergington.edu"},
            {"name": "Amelia", "email": "amelia@mergington.edu"}
        ]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Wednesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": [
            {"name": "Lucas", "email": "lucas@mergington.edu"},
            {"name": "Ella", "email": "ella@mergington.edu"}
        ]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 12,
        "participants": [
            {"name": "James", "email": "james@mergington.edu"},
            {"name": "Grace", "email": "grace@mergington.edu"}
        ]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
async def signup(activity_name: str, email: str = Query(...)):
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    activity = activities[activity_name]
    
    # Normalize email to lowercase
    email = email.lower()
    
    # Check if the student is already registered
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student is already registered for this activity")
    
    # Check if the activity is full
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")
    
    # Add the student if not already registered
    activity["participants"].append(email)
    return {"message": "Signup successful"}