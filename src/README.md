# Mergington High School Activities API

A FastAPI-based application that allows students to view and sign up for extracurricular activities at Mergington High School.

## Features

- View all available extracurricular activities.
- Sign up for activities with email and name.
- Unregister from activities.
- Real-time updates to activity participants.

## Project Structure

- **`app.py`**: The main FastAPI application containing API endpoints and in-memory data storage.
- **`test_app.py`**: Unit tests for the API endpoints using `pytest`.
- **`static/`**: Contains the frontend files (`index.html`, `styles.css`, `app.js`) for the web interface.
- **`requirements.txt`**: Python dependencies for the project.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mergington-activities.git
   cd mergington-activities
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn src.app:app --reload
   ```

4. **Access the application**:
   - API documentation: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Web interface: [http://localhost:8000/static/index.html](http://localhost:8000/static/index.html)

## API Endpoints

| Method | Endpoint                                                          | Description                                                         |
| ------ | ----------------------------------------------------------------- | ------------------------------------------------------------------- |
| GET    | `/activities`                                                     | Retrieve all activities with details and participant information.   |
| POST   | `/activities/{activity_name}/signup?email={email}&name={name}`    | Sign up for an activity.                                            |
| POST   | `/activities/{activity_name}/unregister?email={email}`            | Unregister from an activity.                                        |

### Example Requests

#### Get All Activities
```bash
curl -X GET http://localhost:8000/activities
```

#### Sign Up for an Activity
```bash
curl -X POST "http://localhost:8000/activities/Chess%20Club/signup?email=testuser@mergington.edu&name=Test%20User"
```

#### Unregister from an Activity
```bash
curl -X POST "http://localhost:8000/activities/Chess%20Club/unregister?email=testuser@mergington.edu"
```

## Frontend Features

- **Dynamic Activity List**: Activities are fetched from the API and displayed as cards.
- **Signup Form**: Allows students to sign up for activities.
- **Participant Management**: Displays participants for each activity with options to unregister.

## Running Tests

Run the unit tests using `pytest`:
```bash
pytest src/test_app.py
```

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](../LICENSE) file for details.

---

**Developed by Pratheek Shenoy K**
