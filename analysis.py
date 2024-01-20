import psutil
import time

# Define baseline values (adjust as needed)
baseline_cpu_threshold = 80.0
baseline_memory_threshold = 80.0

def monitor_system():
    while True:
        # Get CPU and memory usage
        cpu_percent = psutil.cpu_percent(interval=1)
        memory_percent = psutil.virtual_memory().percent

        # Check for abnormal CPU usage
        if cpu_percent > baseline_cpu_threshold:
            alert_user("Abnormal CPU usage detected!")

        # Check for abnormal memory usage
        if memory_percent > baseline_memory_threshold:
            alert_user("Abnormal memory usage detected!")

        # Additional checks for abnormal behaviors can be added here

        # Sleep for a short interval before the next check
        time.sleep(5)

def alert_user(message):
    # Replace this with your preferred method of alerting the user
    print("ALERT: " + message)

if __name__ == "__main__":
    monitor_system()
