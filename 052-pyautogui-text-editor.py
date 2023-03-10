import pyautogui as gui
import webbrowser
import random

url = 'your_editor'
text = 'your_text'

print(text)

webbrowser.open(url)

gui.sleep(3)

gui.moveTo(300, 800)

gui.sleep(5)

gui.click()


for t in text:
    gui.write(t, interval=random.choice([0.01,0.03,0.05,0.07,0.09,0.1,0.2,0.3,0.4,0.5]))
              
