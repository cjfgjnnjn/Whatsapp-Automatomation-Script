import pyautogui

print("Move the mouse to the desired position and press Ctrl-C")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Position: ({x}, {y})", end="\r")
except KeyboardInterrupt:
    print("\nDone.")
