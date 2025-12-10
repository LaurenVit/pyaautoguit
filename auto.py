import pyautogui
import time

pyautogui.FAILSAFE = True

time.sleep(3)

pyautogui.click(200, 200) 

pyautogui.hotkey("ctrl", "l")  
time.sleep(0.5)
pyautogui.write("https://www.wikipedia.org")
pyautogui.press("enter")

time.sleep(3)

pyautogui.write("Inteligência Artificial")
pyautogui.press("enter")

pyautogui.click(600, 350)  

time.sleep(3)

screenshot = pyautogui.screenshot()
screenshot.save("resultado_wikipedia.png")
print("Automação finalizada com sucesso!")
