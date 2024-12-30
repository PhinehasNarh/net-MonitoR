# Network Connection Monitoring Script

This Python script monitors the system's internet connection, logs connection statuses, and calculates downtime duration. The logs are saved in a user-specified file path.

## Features
- **Ping Test**: Uses the `8.8.8.8` (Google DNS) server to check connectivity.
- **Log File Creation**: Saves connection events (disconnection, reconnection) to a log file at a custom location.
- **Downtime Calculation**: Calculates and logs the duration of connection unavailability.
- **User-Friendly**: Prompts users for the file path to save the logs.

## Prerequisites
- Python 3.x installed on your system.
- Permissions to write to the specified log file location.

## How to Use
1. Clone or download the script to your local system.
2. Open a terminal and navigate to the script's directory.
3. Run the script:
   ```bash
   python net_monitor.py
   ```
4. When prompted, enter the full file path where you want the log file stored. Example:
   ```
   Enter the full path to store the log file (e.g., C:/logs/networkinfo.log)
   ```

## Log File Example
Below is an example of how logs will look in the specified file:
```
CONNECTION ACQUIRED
Connection acquired at: 2024-12-30 15:11:25

Monitoring started at: 2024-12-30 15:11:25

Disconnected at: 2024-12-30 15:20:10
Connected again at: 2024-12-30 15:22:45
Connection was unavailable for: 0:02:35
```

## How It Works
1. **Ping**: The script sends a ping to `8.8.8.8` to test connectivity.
2. **Monitoring**: Continuously checks the connection and logs the status every 5 seconds.
3. **Downtime**: Calculates how long the connection was unavailable when restored.

## Known Issues
- Ensure the provided file path includes a file name (e.g., `networkinfo.log`), not just a directory.
- The script may require elevated permissions if writing to system-protected locations.

## Contribution
Feel free to fork the repository, make changes, and submit a pull request. Suggestions are always welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.


### #ph1n3y
