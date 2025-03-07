import os
import sys
import winreg as reg

def add_to_registry():
    # Get the path to your Python script
    python_script_path = os.path.abspath(sys.argv[0])

    # Registry path to add auto-start
    registry_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
    registry_value = "ScreenshotApp"
    
    # Access the registry and set the value
    reg.OpenKey(reg.HKEY_CURRENT_USER, registry_key, 0, reg.KEY_WRITE)
    reg.SetValueEx(reg.OpenKey(reg.HKEY_CURRENT_USER, registry_key), registry_value, 0, reg.REG_SZ, python_script_path)

if __name__ == "__main__":
    add_to_registry()
