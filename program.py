import pyautogui
import time
import pyperclip

pyautogui.click(1185,1052)
time.sleep(1)

pyautogui.moveTo(597,164)
pyautogui.dragTo(1768,965,duration=1.0,button='left')

pyautogui.hotkey('ctrl','c')
time.sleep(1)

text=pyperclip.paste()

print(text)
