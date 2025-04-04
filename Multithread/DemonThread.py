import threading
import time

def background_task():
    while True:
        print("Background Task Running...")
        time.sleep(1)

# Create a Demon thread
thread = threading.Thread(target=background_task) ## Threading is a Module and Thread is a Class
thread.daemon = True # Set a thread as a demon
thread.start() # Start Method

print(thread)