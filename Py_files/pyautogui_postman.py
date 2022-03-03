import pyautogui
import random
import string
import time

x = range(1, 120)


def fap():
    characters = string.ascii_letters + string.digits + string.punctuation
    rand_all = ''.join(random.choice(characters) for _ in range(40))
    p = pyautogui.position()
    print(p)
    pyautogui.click(x=943, y=499)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.write(rand_all)
    pyautogui.click(x=1797, y=249)
    time.sleep(1)


for _ in x:
    fap()
