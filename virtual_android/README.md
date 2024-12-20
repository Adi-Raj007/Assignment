
# Virtual Android System Simulation

## Overview
This project simulates a virtual Android environment using QEMU, installs a sample APK, and retrieves system information. It logs all actions to a file for analysis and debugging.

---

## Features
- Simulates a virtual Android environment using QEMU.
- Installs a sample APK into the virtual system.
- Retrieves and logs system information (OS version, device model, and available memory).

---

## Requirements
- Python 3.x
- QEMU installed and configured
- Android Debug Bridge (ADB)
- Android system image (e.g., `path_to_android_image.img`)
- Sample APK file (e.g., `sample_app.apk`)

---

## Project Structure
```
.
├── android_simulation.py    # Main Python script
├── android_system.log       # Log file for system actions
└── README.md                # Documentation
```

---

## Setup

1. **Install QEMU**:
   Follow the official instructions to install QEMU on your system.

2. **Install ADB**:
   ```bash
   sudo apt-get install adb  # For Ubuntu/Debian
   ```

3. **Prepare Android Image**:
   Ensure you have a valid Android image (e.g., `path_to_android_image.img`) and update the `ANDROID_IMAGE` path in the script.

4. **Prepare Sample APK**:
   Place the APK file (e.g., `sample_app.apk`) in the same directory as the script and update the `APK_PATH` in the script.

---

## Running the Simulation

1. **Launch the Simulation**:
   ```bash
   python android_simulation.py
   ```

2. The script will:
   - Start a virtual Android environment.
   - Install the sample APK using ADB.
   - Log system information to `android_system.log`.

---

## Output

- **Log File**:
  The actions and results are logged in `android_system.log`. Example log entries:
  ```
  2024-12-20 12:00:00 - INFO - Virtual Android environment created and launched.
  2024-12-20 12:01:00 - INFO - Sample app installed successfully.
  2024-12-20 12:02:00 - INFO - OS Version: 11
  2024-12-20 12:02:10 - INFO - Device Model: Virtual Pixel 5
  ```

---

## Notes
- Modify the sleep duration (`time.sleep(60)`) based on your system's boot time.
- Ensure ADB is properly configured to connect with the QEMU virtual device.
- Use `KeyboardInterrupt (Ctrl+C)` to terminate the simulation gracefully.

---
