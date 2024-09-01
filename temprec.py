# ------------------------------------------
#  _____                    ____
# |_   _|__ _ __ ___  _ __ |  _ \ ___  ___
#   | |/ _ \ '_ ` _ \| '_ \| |_) / _ \/ __|
#   | |  __/ | | | | | |_) |  _ <  __/ (__
#   |_|\___|_| |_| |_| .__/|_| \_\___|\___|
#                    |_|
# ------------------------------------------

# Importing libraries used
import os
import time
import signal
import csv
from datetime import datetime

# Function to get CPU temperature
def get_cpu_temp():
    temp_output = os.popen("sensors").readlines()
    for line in temp_output:
        if "Core 0:" in line or "CPU:" in line or "Package id 0:" in line:
            parts = line.split()
            for part in parts:
                if "°C" in part:
                    return float(part.replace("°C", "").replace("+", ""))
    raise ValueError("Temperature information not found in sensors output")

# Function to handle the script stop signal
def signal_handler(sig, frame):
    print("\nRecording stopped. Processing data ...")
    if 'csv_file' in globals():
        csv_file.close()
    exit(0)

# Handling Termination Signal
signal.signal(signal.SIGINT, signal_handler)

# Write to csv file as log
csv_file = open("cpu_temp_log.csv", mode="a", newline="")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Time (s)", "Temperature (°C)"])

# Main Loop
print("Recording CPU Temperature. Press Ctrl+C to stop")
start_time = time.time()
while True:
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temp = get_cpu_temp()
        print(f"[{current_time}] Current temperature: {temp:.2f}°C")
        csv_writer.writerow([current_time, temp])
        # Ensure data is written to disk
        csv_file.flush()  
    except ValueError as e:
        print(f"Error: {e}")
    # Adjust the interval as needed
    time.sleep(1)  