import pyautogui
import time

msg="આ મહિને કેટલું પેમેન્ટ ક્લિયર કરાવશો મેસેજ કરો"
count=10

print("You have 5 second to open the whats app")
time.sleep(5)

for i in range(count):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    time.sleep(1.0)