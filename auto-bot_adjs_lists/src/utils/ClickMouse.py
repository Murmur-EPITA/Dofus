import pyautogui

from src.utils.CONSTANTS import *
from src.utils.other import getPercent, random_almost
from src.utils.Player import Player


class ClickMouse:
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self):
        super(ClickMouse, self).__init__()
        self.delay = DELAY_CLICK
        self.program_running = True
        print('ClickMouse created.')

    def go_up(self, window: pyautogui.Window):
        '''
        Go on upper case, y position is decremented by one.
        :param window:
        :param adjs:
        :param player:
        :param direction: if cursor is already up, then move player
        :param windowSize: (int, int)
        :return: None
        '''
        pyautogui.moveTo(x=window.topleft[0] + random_almost(window.size[0] / 2, getPercent(20, window.size[0])),
                         y=window.topleft[1] + random_almost(35, 3),
                         duration=0.5)
        # player.posY.pos -= 1
        pyautogui.click()
        pyautogui.moveTo(x=window.topleft[0] + window.size[0] / 2,
                         y=window.topleft[1] + window.size[1] / 2,
                         duration=0.5)

    def go_right(self, window: pyautogui.Window):
        '''
        Go on right case, x position is incremented by one.
        :param window:
        :param player:
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        pyautogui.moveTo(x=window.topleft[0] + random_almost(window.size[0] - 30, 3),
                         y=window.topleft[1] + random_almost(window.size[1] / 2, getPercent(20, window.size[1])),
                         duration=0.5)
        # player.posX.pos += 1
        pyautogui.click()
        pyautogui.moveTo(x=window.topleft[0] + window.size[0] / 2,
                         y=window.topleft[1] + window.size[1] / 2,
                         duration=0.5)

    def go_down(self, window: pyautogui.Window):
        '''
        Go on lower case, y position is incremented by one.
        :param player:
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        pyautogui.moveTo(x=window.topleft[0] + random_almost(window.size[0] / 2, getPercent(10, window.size[0])),
                         y=window.topleft[1] + window.size[1] - getPercent(window.size[1], 13),
                         duration=0.5)
        # player.posY.pos += 1
        pyautogui.click()
        pyautogui.moveTo(x=window.topleft[0] + window.size[0] / 2,
                         y=window.topleft[1] + window.size[1] / 2,
                         duration=0.5)

    def go_left(self, window: pyautogui.Window):
        '''
        Go on left case, x position is decremented by one.
        :param player:
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        pyautogui.moveTo(x=window.topleft[0] + (random_almost(30, 3)),
                         y=window.topleft[1] + (random_almost(window.size[1] / 2 + 10, getPercent(20, window.size[1]))),
                         duration=0.5)
        # player.posX.pos -= 1
        pyautogui.click()
        pyautogui.moveTo(x=window.topleft[0] + window.size[0] / 2,
                         y=window.topleft[1] + window.size[1] / 2,
                         duration=0.5)

    def go_rel_pos(self, x, y):
        '''
        Move to the actual position of the cursor + parameters.
        newPosX = cursorX + x | newPosY = cursorY + y
        :param x: int
        :param y: int
        :return: None
        '''
        pyautogui.moveRel(x, y, 0.5)
        pyautogui.click()

    def go_abs_pos(self, x, y):
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.click()
