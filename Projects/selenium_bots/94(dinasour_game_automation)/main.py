import pyautogui


pyautogui.FAILSAFE = True
X_VALUE = 470


def bot() -> None:
    """Reads screen and presses space if it's needed when it's activated. You need to run the function and open the link below. Bot will play it by itself.
              https://elgoog.im/dinosaur-game/"""
    try:
        while True:
            if pyautogui.pixelMatchesColor(226, 183, (255, 255, 255)) == True:
                if pyautogui.pixelMatchesColor(X_VALUE, 634, (255, 255, 255)) == False and pyautogui.pixelMatchesColor(X_VALUE, 712, (255, 255, 255)) != False:
                    pyautogui.typewrite(['space'])
                elif pyautogui.pixelMatchesColor(X_VALUE, 712, (255, 255, 255)) == False:
                    pyautogui.typewrite(['space'])
            else:
                if pyautogui.pixelMatchesColor(X_VALUE, 634, (172, 172, 172)) == True and pyautogui.pixelMatchesColor(X_VALUE, 712, (172, 172, 172)) != True:
                    pyautogui.typewrite(['space'])
                elif pyautogui.pixelMatchesColor(X_VALUE, 712, (172, 172, 172)) == True:
                    pyautogui.typewrite(['space'])

    except KeyboardInterrupt:
        print('\n')


def main() -> None:
    bot()


if __name__ == '__main__':
    main()
