import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import plate_database

# Define the function to execute when the file changes
def execute_external_function():
    plate_database.auto_main()

# Define the event handler class
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('cropped_plate.jpg'):
            execute_external_function()

def main():
    # Define the path to monitor
    path = os.path.abspath('.')
    
    # Create the observer
    observer = Observer()
    observer.schedule(MyHandler(), path, recursive=True)
    
    # Start the observer
    observer.start()
    print("Monitoring for changes...")
    
    try:
        while True:
            time.sleep(3)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
