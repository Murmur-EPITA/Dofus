from pynput.mouse import Controller
from threading import Thread

from src.utils.CONSTANTS import *
from src.utils.DIRECTION import *


class ClickMouse(Thread):
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, mouse: Controller):
        super(ClickMouse, self).__init__()
        self.button = Button(BUTTON)
        self.program_running = True
        self.mouse = mouse
        print('ClickMouse created.')

    def go_up(self, windowSize, direction: Direction):
        '''
        Go on upper case, y position is decremented by one.
        :param adjs:
        :param player:
        :param direction: if cursor is already up, then move player
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (windowSize[0] / 2, 45)
        if direction is not None and direction == 0:
            self.mouse.click(button=self.button, count=1)

    def go_right(self, windowSize, direction: Direction):
        '''
        Go on right case, x position is incremented by one.
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (windowSize[0] - 30, windowSize[1] / 2)
        if direction and direction == Direction.RIGHT:
            self.mouse.click(button=self.button, count=1)

    def go_down(self, windowSize, direction: Direction):
        '''
        Go on lower case, y position is incremented by one.
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (windowSize[0] / 2, windowSize[1] - 130)
        if direction and direction == Direction.DOWN:
            self.mouse.click(button=self.button, count=1)

    def go_left(self, windowSize, direction: Direction):
        '''
        Go on left case, x position is decremented by one.
        :param direction:
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (30, windowSize[1] / 2 + 10)
        if direction and direction == Direction.LEFT:
            self.mouse.click(button=self.button, count=1)
