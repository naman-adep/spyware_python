import pyautogui,time 

img = pyautogui.screenshot()
img.save("screenshot.jpg")
time.sleep(5)