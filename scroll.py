import sys
import time
import threading

class Scroll:
    def __init__(self):
        self.enter_pressed = False

    def detect_enter(self):
        input()  # Wait for Enter key press
        self.enter_pressed = True

    def slow_print(self, text, delay=0.1):
        self.enter_pressed = False
        enter_thread = threading.Thread(target=self.detect_enter)
        enter_thread.start()

        for char in text:
            if self.enter_pressed:
                sys.stdout.write(text[text.index(char):])
                sys.stdout.flush()
                break
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)

        print()  # Move to the next line after printing the text

        # Ensure the Enter key press thread has finished
        enter_thread.join()

        # Wait for Enter key press before moving to the next message
        input("Press 'Enter' to continue...")
