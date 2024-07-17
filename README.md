# WhatsApp Automation Script

This Python script automates the process of opening WhatsApp, searching for a contact, and sending messages using `pyautogui` and `pygetwindow`.

## Requirements

Make sure you have the following Python packages installed:

- `pyautogui`
- `pygetwindow`

You can install these packages using pip:

```bash
pip install pyautogui pygetwindow
```

## How to Use

1. **Set Up Coordinates**: 
   - This script relies on specific screen coordinates for clicking on the WhatsApp interface elements (search bar, contacts, message input box).
   - To find these coordinates, you can use a helper script (e.g., `coordinate.py`) that allows you to print the current mouse position. Move your mouse to the desired position and run the script to get the coordinates.
   - Replace the placeholder coordinates in the `search_contact` and `send_message` functions with the actual coordinates obtained.

2. **Edit the Script**:
   - Replace `Contact_Name` in the example usage with the actual contact name you want to message.
   - Modify the `message` variable with the text you wish to send.
   - Change the number in `send_message_multiple_times(contact_name, message, 1)` to specify how many times you want to send the message.

3. **Run the Script**:
   - Execute the script in your Python environment. Make sure WhatsApp is already installed and you are logged in.
   - The script will open WhatsApp, maximize the window, search for the specified contact, and send the designated message the specified number of times.
## Example Usage

```python
contact_name = "John Doe"  # Replace with the actual contact name
message = "Hello, this is an automated message!"
send_message_multiple_times(contact_name, message, 3)  # Send the message 3 times
```
## Notes

- Ensure that your screen resolution and scaling settings are consistent when running the script, as coordinates are pixel-specific.
- Adjust the `time.sleep()` durations as needed to ensure WhatsApp loads completely before performing the next action.

## Disclaimer

Use this script responsibly. Automated messaging may violate WhatsApp's terms of service, and excessive use could lead to account restrictions.


