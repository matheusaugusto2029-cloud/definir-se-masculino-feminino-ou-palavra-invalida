import pyautogui
import time
pyautogui. PAUSE = 2
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("noticias do mundo")
pyautogui.press("enter")
pyautogui.moveTo(x=978, y=448)
for i in range (10):
 pyautogui.scroll(-200)
 time.sleep(1)