from pynput.mouse import Controller
from threading import Thread
from time import sleep

from src.utils.CONSTANTS import *
from src.utils.DIRECTION import *
from src.utils.other import getPercent, random_almost
from src.utils.Player import Player


class ClickMouse:
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, mouse: Controller):
        super(ClickMouse, self).__init__()
        self.delay = DELAY_CLICK
        self.button = Button(BUTTON)
        self.start_and_stop = False
        self.program_running = True
        self.mouse = mouse
        print('ClickMouse created.')


    def start_clicking(self):
        self.start_and_stop = True

    def stop_clicking(self):
        self.start_and_stop = False

    def go_up(self, windowSize, player: Player):
        '''
        Go on upper case, y position is decremented by one.
        :param adjs:
        :param player:
        :param direction: if cursor is already up, then move player
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (random_almost(windowSize[0] / 2, getPercent(20, windowSize[0])), random_almost(35, 3))
        player.posY.pos -= 1
        self.mouse.click(button=self.button, count=1)
        self.mouse.position = (windowSize[0] / 2, windowSize[1] / 2)

    def go_right(self, windowSize, player: Player):
        '''
        Go on right case, x position is incremented by one.
        :param player:
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (random_almost(windowSize[0] - 30, 3), random_almost(windowSize[1] / 2), getPercent(20, windowSize[1]))
        player.posX.pos += 1
        self.mouse.click(button=self.button, count=1)
        self.mouse.position = (windowSize[0] / 2, windowSize[1] / 2)

    def go_down(self, windowSize, player: Player):
        '''
        Go on lower case, y position is incremented by one.
        :param player:
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (random_almost(windowSize[0] / 2, getPercent(20, windowSize[0])), windowSize[1] - getPercent(windowSize[1], 13))
        player.posY.pos += 1
        self.mouse.click(button=self.button, count=1)
        self.mouse.position = (windowSize[0] / 2, windowSize[1] / 2)

    def go_left(self, windowSize, player: Player):
        '''
        Go on left case, x position is decremented by one.
        :param player:
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (random_almost(30, 3), random_almost(windowSize[1] / 2 + 10), getPercent(20, windowSize[1]))
        player.posX.pos -= 1
        self.mouse.click(button=self.button, count=1)
        self.mouse.position = (windowSize[0] / 2, windowSize[1] / 2)

    def go_rel_pos(self, x, y):
        '''
        Move to the actual position of the cursor + parameters.
        newPosX = cursorX + x | newPosY = cursorY + y
        :param x: int
        :param y: int
        :return: None
        '''
        self.mouse.move(x, y)
        self.mouse.click(button=self.button, count=1)

    def go_abs_pos(self, x, y):
        self.mouse.position = (x, y)
        self.mouse.click(button=self.button, count=1)

    def exit(self):
        self.stop_clicking()
        self.program_running = False
