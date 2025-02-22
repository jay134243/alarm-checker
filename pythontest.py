import time
from datetime import datetime
import platform

if platform.system() == "Windows":
    import winsound
else:
    def winsound_beep(frequency, duration):
        print(f"Beep at {frequency}Hz for {duration}ms")
    winsound = type('winsound', (object,), {'Beep': winsound_beep})()

# Define a list to store the tasks and their corresponding alarm times
todo_list = [
    ("Wake up", "07:00"),
    ("Exercise", "07:30"),
    ("Breakfast", "08:00"),
    ("Shower", "08:30"),
    ("Start work", "09:00"),
    ("Test Alarm", datetime.now().strftime("%H:%M"))  # Add a task with the current time for testing
]

def check_alarms():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        for task, alarm_time in todo_list:
            if current_time == alarm_time:
                print(f"Alarm for task: {task}")
                winsound.Beep(1000, 1000)  # Sound the alarm
        time.sleep(60)  # Check every minute

print("Starting alarm check...")
# Start checking alarms
check_alarms()
