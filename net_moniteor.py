import os
import socket
import datetime
import time

FILE = input("Enter the full path to store the log file (e.g., C:/logs/networkinfo.log): ")

os.makedirs(os.path.dirname(FILE), exist_ok=True)

def ping():
    try:
        socket.setdefaulttimeout(3)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "8.8.8.8"
        port = 53
        s.connect((host, port))
    except OSError:
        return False
    else:
        s.close()
        return True

def calculate_time(start, stop):
    """Calculates the duration between two timestamps."""
    difference = stop - start
    seconds = float(difference.total_seconds())
    return str(datetime.timedelta(seconds=seconds)).split(".")[0]

def first_check():
    if ping():
        live = "\nCONNECTION ACQUIRED\n"
        print(live)
        connection_acquired_time = datetime.datetime.now()
        acquiring_message = "Connection acquired at: " + str(connection_acquired_time).split(".")[0]
        print(acquiring_message)
        with open(FILE, "a") as file:
            file.write(live)
            file.write(acquiring_message + "\n")
        return True
    else:
        not_live = "\nCONNECTION NOT ACQUIRED\n"
        print(not_live)
        with open(FILE, "a") as file:
            file.write(not_live)
        return False

def main():
    """Main function to monitor network connection."""
    monitor_start_time = datetime.datetime.now()
    monitoring_date_time = "Monitoring started at: " + str(monitor_start_time).split(".")[0]
    
    if first_check():
        print(monitoring_date_time)
        with open(FILE, "a") as file:
            file.write("\n" + monitoring_date_time + "\n")
    else:
        while not ping():
            time.sleep(1)
        first_check()
        print(monitoring_date_time)
        with open(FILE, "a") as file:
            file.write("\n" + monitoring_date_time + "\n")

    while True:
        if ping():
            time.sleep(5)
        else:
            down_time = datetime.datetime.now()
            fail_msg = "Disconnected at: " + str(down_time).split(".")[0]
            print(fail_msg)
            with open(FILE, "a") as file:
                file.write(fail_msg + "\n")
            
            while not ping():
                time.sleep(1)
            
            up_time = datetime.datetime.now()
            uptime_message = "Connected again at: " + str(up_time).split(".")[0]
            down_duration = calculate_time(down_time, up_time)
            unavailability_time = "Connection was unavailable for: " + down_duration
            print(uptime_message)
            print(unavailability_time)
            with open(FILE, "a") as file:
                file.write(uptime_message + "\n")
                file.write(unavailability_time + "\n")

if __name__ == "__main__":
    main()

#ph1n3y
