import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_activity_success():
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "testuser@mergington.edu", "name": "Test User"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Signup successful"

def test_signup_activity_not_found():
    response = client.post(
        "/activities/Nonexistent Activity/signup",
        params={"email": "testuser@mergington.edu", "name": "Test User"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

def test_signup_activity_already_registered():
    client.post(
        "/activities/Chess Club/signup",
        params={"email": "testuser@mergington.edu", "name": "Test User"}
    )
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "testuser@mergington.edu", "name": "Test User"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already registered for this activity"

def test_signup_activity_full():
    for i in range(12):  # Max participants for Chess Club is 12
        client.post(
            "/activities/Chess Club/signup",
            params={"email": f"user{i}@mergington.edu", "name": f"User {i}"}
        )
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "overflow@mergington.edu", "name": "Overflow User"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"

def test_unregister_activity_success():
    client.post(
        "/activities/Chess Club/signup",
        params={"email": "testuser@mergington.edu", "name": "Test User"}
    )
    response = client.post(
        "/activities/Chess Club/unregister",
        params={"email": "testuser@mergington.edu"}
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistration successful"

def test_unregister_activity_not_found():
    response = client.post(
        "/activities/Nonexistent Activity/unregister",
        params={"email": "testuser@mergington.edu"}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

def test_unregister_activity_not_registered():
    response = client.post(
        "/activities/Chess Club/unregister",
        params={"email": "notregistered@mergington.edu"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not registered for this activity"
