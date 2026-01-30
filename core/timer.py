import time
import threading
import keyboard

def timer():
    duration_in_seconds = 0
    paused = threading.Event()
    paused.clear()

    def check_pause():
        while True:
            if keyboard.is_pressed('p'):
                paused.set()
                print("Paused. Press 'r' to resume.")
                while not keyboard.is_pressed('r'):
                    time.sleep(0.1)
                paused.clear()
                print("Resumed.")
            time.sleep(0.1)

    threading.Thread(target=check_pause, daemon=True).start()

    print("Press 'p' to pause, 'r' to resume.")
    while True:
        if not paused.is_set():
            time.sleep(1)
            duration_in_seconds += 1
            print(duration_in_seconds)
        else:
            time.sleep(0.1)

if __name__ == "__main__":
    timer()