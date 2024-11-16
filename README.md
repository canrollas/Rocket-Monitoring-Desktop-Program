# Rocket Monitoring Desktop App

## Overview

The **Rocket Monitoring Desktop App** is a Python-based application built using PyQt5 (or PySide2) for real-time monitoring of a rocket's key telemetry data. The app provides a user-friendly interface for tracking and visualizing essential parameters during rocket tests and flights.

## Features

- **GPS Tracking:** Displays the rocket's real-time location and movement path on an integrated map.
- **Ignition Monitoring:** Tracks the ignition state and logs ignition events.
- **Acceleration:** Shows real-time acceleration data in all axes.
- **Speed Monitoring:** Displays the rocket's velocity over time.
- **Gyroscope Data:** Monitors and visualizes orientation changes using gyroscopic readings.
- **Altitude Monitoring:** Tracks the rocket's height above ground level in real time.
- **Real-Time Graphs:** Visual representation of telemetry data, including speed, altitude, and acceleration.
- **Data Logging:** Automatically logs all telemetry data for post-flight analysis.
- **Custom Alerts:** Set thresholds for parameters to trigger alerts for critical conditions.

## Technology Stack

- **Programming Language:** Python
- **Framework:** PyQt5 (or PySide2)
- **Data Visualization:** Matplotlib, PyQtGraph
- **Backend:** SQLite (for data logging) or custom log file formats
- **Hardware Communication:** Serial/USB/UART for telemetry data
- **Map Integration:** OpenStreetMap or Google Maps API (optional)

## Installation

### Prerequisites

- Python 3.8+
- PyQt5 (or PySide2)
- Matplotlib
- PyQtGraph
- Numpy
- PySerial (for hardware communication)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/rocket-monitoring-app.git
   cd rocket-monitoring-app
