import pyautogui 
import time
comments=["partaji","fares","fares",]
time.sleep(5)
for i in range(100):
   pyautogui.typewrite(comments[i%3])
   pyautogui.typewrite("\n")
   time.sleep(2)
