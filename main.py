from time import sleep

import pyautogui

pyautogui.FAILSAFE = True

FIREFOX_ICON = (38, 153)
FIREFOX_URL = (639, 113)
FIREFOX_FOLLOW_LINKS = (1059,111)

CODEBY_BUTTON_LOGIN = (1081, 194)
CODEBY_BUUTON_PASSWORD = (964,380)
CODEBY_BUUTON_AUTH = (947,514)

def openBrowser():
    sleep(5)
    button_POSTMAN = pyautogui.locateCenterOnScreen('POSTMAN.png')
    print(button_POSTMAN)
    pyautogui.click(button_POSTMAN)
    pyautogui.click(button_POSTMAN)
    sleep(10)
    # pyautogui.click(FIREFOX_URL)
    # pyautogui.hotkey('ctrl', 'a')
    # pyautogui.keyDown('backspace')
    # print("Open site Codeby.net")
    # pyautogui.typewrite('https://codeby.net/')
    # pyautogui.click(FIREFOX_FOLLOW_LINKS)
    # sleep(2)


if __name__ == '__main__':
    openBrowser()