
# Flask API for App Management

## Overview
This project provides a simple Flask-based API for managing app details. It supports adding, retrieving, and deleting records, with SQLite as the database backend.

---

## Features
- Add app details (app name, version, description).
- Retrieve app details by their ID.
- Delete an app by its ID.

---

## Requirements
- Python 3.x
- Flask
- SQLite

---

## Project Structure
```
.
├── app.py              # Main Flask application
├── schema.sql          # SQLite schema file
├── sample_data.sql     # Sample data for database
└── README.md           # Documentation
```

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Initialize the database:**
   The database is initialized automatically when you run the app. Ensure `schema.sql` and `sample_data.sql` are present in the same directory as `app.py`.

---

## Running the Application

Start the Flask application:
```bash
python app.py
```

The API will be accessible at `http://127.0.0.1:5000`.

---

## API Endpoints

### 1. Add App
**Endpoint:**
`POST /add-app`

**Request Body (JSON):**
```json
{
  "app_name": "ExampleApp",
  "version": "1.0",
  "description": "An example app."
}
```

**Response:**
- `201`: App successfully added.

---

### 2. Get App
**Endpoint:**
`GET /get-app/<app_id>`

**Response:**
- `200`: App details retrieved successfully.
- `404`: App with the given ID not found.

---

### 3. Delete App
**Endpoint:**
`DELETE /delete-app/<app_id>`

**Response:**
- `200`: App deleted successfully.
- `404`: App with the given ID not found.

---

## Example API Usage

### Add App:
```bash
curl -X POST http://127.0.0.1:5000/add-app \
-H "Content-Type: application/json" \
-d '{"app_name": "MyApp", "version": "1.0", "description": "Test app"}'
```

### Get App:
```bash
curl -X GET http://127.0.0.1:5000/get-app/1
```

### Delete App:
```bash
curl -X DELETE http://127.0.0.1:5000/delete-app/1
```

---

## Database Schema
**Table Name:** `apps`
| Column Name   | Type     | Description                       |
|---------------|----------|-----------------------------------|
| `id`          | INTEGER  | Primary key (auto-incremented).  |
| `app_name`    | TEXT     | Name of the app.                 |
| `version`     | TEXT     | Version of the app.              |
| `description` | TEXT     | Description of the app.          |

---

## Notes
- The database file (`database.db`) will be created automatically in the working directory.
- Ensure `schema.sql` contains the correct table definitions.
