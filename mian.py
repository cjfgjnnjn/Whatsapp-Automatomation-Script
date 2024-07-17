import pyautogui
import pygetwindow as gw
import time

def open_whatsapp():
    # Click on the Windows button
    pyautogui.press('win')
    time.sleep(1)
    
    # Type 'WhatsApp'
    pyautogui.write('WhatsApp', interval=0.1)
    time.sleep(1)
    
    # Press 'Enter' to open WhatsApp
    pyautogui.press('enter')
    time.sleep(5)  # Adjust the delay if necessary for WhatsApp to open

def maximize_whatsapp():
    # Get the WhatsApp window
    whatsapp_window = None
    for window in gw.getWindowsWithTitle('WhatsApp'):
        if 'WhatsApp' in window.title:
            whatsapp_window = window
            break
    
    if whatsapp_window:
        # Maximize the WhatsApp window
        whatsapp_window.maximize()
        # Bring the WhatsApp window to the foreground
        whatsapp_window.activate()
        time.sleep(2)  # Wait for the window to maximize and come to the foreground

def search_contact(contact_name):
    # Click on the search bar (Adjust coordinates as needed)
    pyautogui.click(x=176, y=106)  # Adjust the coordinates for the search bar accordingly
    time.sleep(1)
    
    # Type the contact name
    pyautogui.write(contact_name, interval=0.1)
    time.sleep(2)  # Wait for search results to appear

    # Click on the first search result (Adjust coordinates as needed)
    pyautogui.click(x=238, y=182)  # Adjust the coordinates for the first contact usingh coordinate.py
    time.sleep(2)

def send_message(message):
    # Click on the message input box (Adjust coordinates as needed)
    pyautogui.click(x=750, y=1000)  # Adjust coordinates for the input box
    time.sleep(1)
    
    # Type the message
    pyautogui.write(message, interval=0)
    
    # Press 'Enter' to send the message
    pyautogui.press('enter')

def send_message_multiple_times(contact_name, message, count):
    open_whatsapp()
    maximize_whatsapp()
    search_contact(contact_name)
    for _ in range(count):
        send_message(message)
        time.sleep(1)  # Add a short delay between messages if needed

# Example usage
contact_name = "Contact_Name " # Replace with the actual contact name
message = "Message"
send_message_multiple_times(contact_name, message, 1)  # Change 1 to the number of times you want to send the message
