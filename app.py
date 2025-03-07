import pyautogui
from PIL import Image, ImageOps
import pystray
from pystray import MenuItem as item
import threading
import time
import sys

# Function to capture screenshot
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

# Function to add a custom border
def add_border(image, border_width=20, border_color=(0, 0, 0)):
    return ImageOps.expand(image, border=border_width, fill=border_color)

# Main function that will run the screenshot capture and border adding
def take_screenshot():
    print("Capturing screenshot...")
    screenshot = capture_screenshot()
    bordered_image = add_border(screenshot, border_width=30, border_color=(255, 0, 0))  # Red border
    bordered_image.save("screenshot_with_border.png")
    bordered_image.show()  # Opens the image in default viewer
    print("Screenshot saved as screenshot_with_border.png")

# Function that will allow the app to always be running
def on_quit(icon, item):
    icon.stop()

# Function to show the system tray icon
def create_tray_icon():
    icon_image = Image.open("icon.png")  # Ensure to have a small icon file in the same directory
    icon = pystray.Icon("screenshot_border", icon_image, "Screenshot Border App", menu=pystray.Menu(
        item("Take Screenshot", lambda icon, item: take_screenshot()),
        item("Quit", on_quit)
    ))
    icon.run()

# Function to start the app
def start_app():
    print("Starting Screenshot Border App...")
    # Run the system tray in a separate thread to keep the app working
    threading.Thread(target=create_tray_icon, daemon=True).start()
    
    # Keep the program running to listen for events
    while True:
        time.sleep(1)

if __name__ == "__main__":
    start_app()
