import pyautogui
import time

pyautogui.PAUSE = 0.01
time.sleep(5)
f = open('beemovie.txt', 'r')
for word in f.readlines():
    if not word.strip():
        continue
    if word:
        pyautogui.typewrite(word)
        pyautogui.press('enter')
