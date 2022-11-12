import pyautogui
import numpy as np
from re import search
from pyautogui import screenshot, Window
from threading import Thread
from time import sleep
import cv2
import pytesseract

from src.utils.other import getPercent
from src.utils.Player import Player
from src.object_recognition import ObjectRecognition


def take_screenshot(window: Window):
    filename = "src/img/screenshots/pos.png"
    screenshot(filename, region=(window.topleft[0] + 8,
                                 window.topleft[1] + 34,
                                 window.topleft[0] + getPercent(50, window.size[0]),
                                 window.topleft[1] + getPercent(10, window.size[1]),
                                 ))
    return filename


def stop_for_x_seconds():
    ret = pyautogui.prompt(text='Position not recognized, enter number of seconds to deactivate pos scanner:', default=5)
    sleep(int(ret))


def check_minus(x: str) -> str:
    if x[0] == '~':
        x = x.replace('~', '-', 1)
    elif x[0] == ':':
        x = x.replace(':', '-', 1)
    elif x[0] == ';':
        x = x.replace(';', '-', 1)
    elif x[0] == '"':
        x = x.replace('"', '-', 1)
    elif x[0] == '“':
        x = x.replace('“', '-', 1)
    return x


def get_square_infos(window: Window):
    """
    OCR to detect square information, particularly player's position.
    :return: x: int, y: int, city: str, place: str
    """

    if window.isMinimized:
        window.activate()
        window.restore()
    image = cv2.imread(take_screenshot(window))
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    def trim(frame):
        # crop top
        if not np.sum(frame[0]):
            return trim(frame[1:])
        # crop bottom
        elif not np.sum(frame[-1]):
            return trim(frame[:-1])
        # crop left
        elif not np.sum(frame[:, 0]):
            return trim(frame[:, 1:])
            # crop right
        elif not np.sum(frame[:, -1]):
            return trim(frame[:, :-1])
        return frame

    sensitivity = 30
    lower_white = np.array([0, 0, 255 - sensitivity])
    upper_white = np.array([255, sensitivity, 255])
    mask = cv2.inRange(hsv, lower_white, upper_white)

    mask = trim(mask)
    mask = cv2.copyMakeBorder(mask, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=0)
    cv2.imwrite('src/img/screenshots/pos_final.png', mask)

    text: str = pytesseract.image_to_string(mask)
    with open('src/img/screenshots/last_pos.txt', 'w') as file:
        file.write(text)

    try:
        tmp = text.split('\n')
        firstLine: str = tmp[0]
        secondLine: str = tmp[1]

        result = search(r"([\w\séèêàâîïûü’']+).[{(](.+)[})]", firstLine)
        if result is None:
            result = search(r"([\w\séèêàâîïûü’']+).{1,2}[{(]?(.+)[})]?", firstLine)

        city: str = result.group(1)
        place: str = result.group(2)
        print(city, place)

        result = search(r"([-~:;\"“]?[\d]+)[,;|\[\]:] ?([-~:;]?[\d]+)", secondLine)
        x: str = result.group(1)
        y: str = result.group(2)
        x, y = check_minus(x), check_minus(y)
        x: int = int(x)
        y: int = int(y)
        print("New pos detected:", x, y)
        return x, y, city, place

    except:
        print('Screenshot is not usable.')
        pyautogui.alert(text='Error while scanning position: get invalid format: ', title='OCR error')


class ScreenScanner(Thread):
    def __init__(self, player: Player):
        Thread.__init__(self)
        self.player = player
        self.running = True
        print('ScreenScanner initialized.')

    def exit(self):
        self.running = False

    def run(self):
        while self.running:
            try:
                self.player.posX.pos, self.player.posY.pos, city, place = get_square_infos(
                    self.player.windowManagement.window)
            except TypeError:
                try:
                    self.player.posX.pos, self.player.posY.pos, city, place = get_square_infos(
                        self.player.windowManagement.window)
                except TypeError:
                    stop_for_x_seconds()
            pos = ObjectRecognition.recognize(self.player.windowManagement.window)
            print(pos)
            if pos is not None:
                pyautogui.click(pos)
            sleep(3)
