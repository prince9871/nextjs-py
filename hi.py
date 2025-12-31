import pyautogui
import time
import random

pyautogui.FAILSAFE = False

while True:
    # Move mouse randomly
    x = random.randint(100, 1000)
    y = random.randint(100, 700)
    pyautogui.moveTo(x, y, duration=0.5)

    # Random small mouse move
    pyautogui.moveRel(random.randint(-20,20), random.randint(-20,20), duration=0.2)

    # Press random key
    key = random.choice(['shift', 'ctrl', 'alt', 'space'])
    pyautogui.press(key)

    # Random delay
    time.sleep(random.randint(5, 10)) 
