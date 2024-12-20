
# Networking Script for Virtual Android System

## Overview
This project connects a virtual Android system to a backend API. It sends mock data about the virtual system and logs the server's responses.

---

## Features
- Sends mock data (app details) from a virtual Android system to the backend API.
- Logs the server's responses and errors in a log file.

---

## Requirements
- Python 3.x
- `requests` library (Install via `pip install requests`)

---

## Project Structure
```
.
├── network_script.py    # Main Python script
├── network.log          # Log file for network actions
└── README.md            # Documentation
```

---

## Setup

1. **Install Dependencies**:
   ```bash
   pip install requests
   ```

2. **Configure Backend API**:
   Ensure the backend API is running at `http://127.0.0.1:5000`. Update the `API_URL` in `network_script.py` if the API is hosted at a different address.

---

## Running the Script

1. **Launch the Script**:
   ```bash
   python network_script.py
   ```

2. The script will:
   - Send mock data (app details) to the backend API.
   - Log the results in `network.log`.

---

## Mock Data Sent
```json
{
  "app_name": "VirtualAndroidApp",
  "version": "1.0",
  "description": "Mock data from virtual Android system"
}
```

---

## Output

- **Log File**:
  All actions and server responses are logged in `network.log`. Example log entries:
  ```
  2024-12-20 12:00:00 - INFO - Successfully sent data: {'app_name': 'VirtualAndroidApp', 'version': '1.0', 'description': 'Mock data from virtual Android system'}
  2024-12-20 12:00:01 - INFO - Server Response: {'id': 1, 'app_name': 'VirtualAndroidApp', 'version': '1.0', 'description': 'Mock data from virtual Android system'}
  ```

---

## Notes
- Ensure the backend API is running before executing the script.
- Logs are saved in `network.log` for debugging and verification.

---
