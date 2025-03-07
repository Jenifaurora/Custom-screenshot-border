https://i.imgur.com/hlAmTA1.png

Firstly, the directory ahem:

```
ScreenshotBorderApp/
│
├── app.py                  # Main Python application file
├── icon.png                # Icon for the system tray (small 16x16 PNG file)
└── startup.py              # Optional file for adding app to Windows startup (if using Windows)
```


1. **Install Dependencies**
   Make sure you have the required Python libraries installed. Open a terminal (or command prompt) and run the following:

   ```bash
   pip install pyautogui pillow pystray
   ```

2. **Step 3: Start the Application ^v^**

   - **For Windows**: 
     - You can manually run `app.py` from the command line by navigating to your directory:
       ```bash
       python app.py
       ```
     - If you want the app to start automatically when Windows boots, run `startup.py` once. This will add it to the startup registry, and it will start automatically the next time you boot your computer.

   - **For macOS/Linux**: 
     - You can run `app.py` manually using the following command:
       ```bash
       python3 app.py
       ```
     - You can also set it to start automatically at boot by creating a service or using `launchd` (macOS) or `systemd` (Linux), similar to what we discussed earlier.

4. **Step 4: Check the System Tray**
   After running the script, you should see an icon in the system tray. Right-click the icon to either take a screenshot or quit the app.
