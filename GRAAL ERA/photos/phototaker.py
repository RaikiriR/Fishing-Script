import pyautogui
import time
import keyboard

def main():
    pyautogui.FAILSAFE = True

    startup()
    picture()

def startup():
    while True:
        try:
            if keyboard.is_pressed('z'):
                picture()
        except:
            break
        

def picture():
    image = pyautogui.screenshot()
    image.save(r"C:\Users\Justin Ching\Desktop\GRAAL ERA\photos\stage.png")

if __name__ == "__main__":
    main()  