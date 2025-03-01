import pyautogui
import keyboard
import time

pyautogui.keyDown("Win")
pyautogui.press("r")
pyautogui.keyUp("Win")
pyautogui.typewrite("https://www.youtube.com/watch?v=xvFZjo5PgG0")
pyautogui.press("enter")
time.sleep(5)
pyautogui.press("f")
