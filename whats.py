import pyautogui
import time
time.sleep(4)
count=0
while count<=100:
    pyautogui.typewrite("happy new year"+str (count))
    pyautogui.press("enter")
    count=count+1