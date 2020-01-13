import pyautogui
import time
import keyboard

def main():
    pyautogui.FAILSAFE = True
    time.sleep(3)
    pyautogui.press('ctrl')
    while True:
        if pyautogui.locateOnScreen(r"C:\Users\Justin Ching\Desktop\GRAAL ERA\photos\bobble.png",confidence=.7) == None:
            time.sleep(1)
            pyautogui.keyDown('d')
            time.sleep(.04)
            pyautogui.keyUp('d')
            time.sleep(2)
            waitFish()
        else:
            time.sleep(1)
        
    
def waitFish():
    while True:
        if pyautogui.locateOnScreen(r"C:\Users\Justin Ching\Desktop\GRAAL ERA\photos\bobble.png",confidence=.7) == None:
            print("Hit")
            pyautogui.click()
            main()


if __name__ == "__main__":
    main()