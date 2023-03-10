import pyautogui as gui

def actions():
    screenWidth, screenHeight = gui.size()
    gui.moveTo(5,screenHeight-5)
    gui.click()

actions()

gui.sleep(1)

actions()
