
# Python Intern Assignment

## Overview
This project is a part of a Python intern assignment. It includes three main components:
1. **Backend API**: A Flask-based API for managing app details (adding, retrieving, and deleting records).
2. **Virtual Android System Simulation**: Simulates a virtual Android environment, installs a sample APK, and retrieves system information.
3. **Networking Script**: Connects the virtual Android system to the backend API to send mock data and log responses.

---

## Features
### 1. Backend API
- Add app details (name, version, description).
- Retrieve app details by ID.
- Delete app details by ID.

### 2. Virtual Android System Simulation
- Simulates a virtual Android environment using QEMU.
- Installs a sample APK into the environment.
- Retrieves and logs system information (e.g., OS version, device model, available memory).

### 3. Networking Script
- Sends mock data from the virtual Android system to the backend API.
- Logs server responses for debugging.

---

## Requirements
- Python 3.x
- Flask (`pip install flask`)
- QEMU (for the virtual Android system)
- ADB (Android Debug Bridge)
- `requests` library (`pip install requests`)

---

## Project Structure
```
.
├── app.py                  # Flask API code
├── android_simulation.py   # Virtual Android system simulation script
├── network_script.py       # Networking script
├── schema.sql              # SQLite database schema
├── sample_data.sql         # Sample data for the database
├── android_system.log      # Log file for Android simulation
├── network.log             # Log file for networking actions
└── README.md               # Documentation
```

---

## Setup and Usage

### 1. Backend API
1. **Install Dependencies**:
   ```bash
   pip install flask
   ```
2. **Initialize the Database**:
   The database is set up automatically when you run the API.
3. **Run the API**:
   ```bash
   python app.py
   ```
4. The API will be available at `http://127.0.0.1:5000`.

---

### 2. Virtual Android System Simulation
1. **Install QEMU and ADB**:
   - Install QEMU following its official instructions.
   - Install ADB:
     ```bash
     sudo apt-get install adb  # For Ubuntu/Debian
     ```
2. **Update Paths in the Script**:
   - Replace `path_to_android_image.img` with the actual path to your Android image.
   - Place `sample_app.apk` in the same directory or update its path in `android_simulation.py`.
3. **Run the Simulation**:
   ```bash
   python android_simulation.py
   ```
4. Logs are saved in `android_system.log`.

---

### 3. Networking Script
1. **Install Dependencies**:
   ```bash
   pip install requests
   ```
2. **Ensure Backend API is Running**:
   Confirm the backend API is running at `http://127.0.0.1:5000`.
3. **Run the Script**:
   ```bash
   python network_script.py
   ```
4. Logs are saved in `network.log`.

---

## API Endpoints (From Backend API)
### Add App
**Endpoint**: `POST /add-app`
**Request Body (JSON)**:
```json
{
  "app_name": "ExampleApp",
  "version": "1.0",
  "description": "An example app."
}
```

### Get App
**Endpoint**: `GET /get-app/<app_id>`

### Delete App
**Endpoint**: `DELETE /delete-app/<app_id>`

---

## Notes
- Ensure all dependencies are installed before running the scripts.
- The backend API must be running before executing the networking script.
- Use the provided log files (`android_system.log` and `network.log`) for debugging.

---
