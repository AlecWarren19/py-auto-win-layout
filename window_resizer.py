import ctypes
import pygetwindow
import pyautogui
from screeninfo import get_monitors
from jsmin import jsmin
from time import sleep

monitors = get_monitors()
#print(monitors)

# # user inputs # #
targets = ["spotify", "discord"]
profile = {
    "spotify" : {"height":0.4, "screen":'l'},
    "discord" : {"height":0.6, "screen":'l'},
}

screen_names = ['m', 'l', 'r']
screens = {
    screen_names[i]: {
        "origin": (monitors[i].x, monitors[i].y),
        "width": None,
        "height": None,
        "occ_w": 0.0,
        "occ_h": 0.0
    } 
    for i in range(len(screen_names))
}

# takes in a screen dict and a window (Win32Window) object
def get_screen_info(screen, win):

    win.restore()
    win.restore()
    win.resizeTo(100, 100)
    win.moveTo(screen["origin"][0] + 100, screen["origin"][1] + 100)
    print("moved win:\n", win)
    win.maximize()
    print("max'd win:\n", win)
    screen["width"] = win.width - 16
    screen["height"] = win.height - 16
    screen["origin"] = (win.left + 8, win.top + 8)

# calculate
get_screen_info(screens[profile[targets[-1]]["screen"]], pygetwindow.getWindowsWithTitle(targets[-1])[0])

for target in targets:
    while target == "spotify" and not pygetwindow.getWindowsWithTitle(target):
        pyautogui.press("playpause")
        sleep(.1)
    if wins:=pygetwindow.getWindowsWithTitle(target):
        for win in wins:
            screen = screens[profile[target]["screen"]]
            # if this screen's info has not been filled out before
            if not screen.get("width"):
                get_screen_info(screen, win)
                
            win.restore()
            
            new_w = (int) (screen["width"] * (occ_w:=(1.0 if not "width" in profile[target] else profile[target]["width"])))
            new_h = (int) (screen["height"] * (occ_h:=(1.0 if not "height" in profile[target] else profile[target]["height"])))
            win.resizeTo(new_w, new_h)

            new_x = screen["origin"][0]
            if screen["occ_w"] + occ_w <= 1.0:
                new_x += (int) (screen["width"] * screen["occ_w"]) 
            
            new_y = screen["origin"][1]
            if new_x == screen["origin"][0] and screen["occ_h"] + occ_h <= 1.0:
                new_y += (int) (screen["height"] * screen["occ_h"])
            screen["occ_w"] = min(1, screen["occ_w"] + occ_w)
            screen["occ_h"] = min(1, screen["occ_h"] + occ_h)
            win.moveTo(new_x, new_y)
            print(target, '\n', win)
            print(profile[target]["screen"], '\n', screen)

"""
print("spotify: \n", pygetwindow.getWindowsWithTitle('spotify')[0])
print("discord: \n", pygetwindow.getWindowsWithTitle('discord')[0])
print("steam: \n", pygetwindow.getWindowsWithTitle('steam')[0])
"""


