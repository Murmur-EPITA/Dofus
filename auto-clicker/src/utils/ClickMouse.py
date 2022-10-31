from collections import deque
from pynput.mouse import Button
from pynput.mouse import Controller
from threading import Thread
from time import sleep

from src.utils.CONSTANTS import *
from src.utils.randomize import random_between as rb


class ClickMouse(Thread):
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, mouse: Controller, queue: deque):
        super(ClickMouse, self).__init__()
        self.delay = DELAY_CLICK
        self.button = Button(BUTTON)
        self.start_and_stop = False
        self.program_running = True
        self.mouse = mouse
        self.queue = queue
        print('ClickMouse created.')

    def start_clicking(self):
        self.start_and_stop = True

    def stop_clicking(self):
        self.start_and_stop = False

    def go_up(self, windowSize):
        '''
        Go on upper case, y position is decremented by one.
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (windowSize[0] / 2, 45)
        if not self.start_and_stop:
            self.mouse.click(button=self.button, count=1)

    def go_right(self, windowSize):
        '''
        Go on right case, x position is incremented by one.
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (windowSize[0] - 30, windowSize[1] / 2)
        if not self.start_and_stop:
            self.mouse.click(button=self.button, count=1)

    def go_down(self, windowSize):
        '''
        Go on lower case, y position is incremented by one.
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (windowSize[0] / 2, windowSize[1] - 130)
        if not self.start_and_stop:
            self.mouse.click(button=self.button, count=1)

    def go_left(self, windowSize):
        '''
        Go on left case, x position is decremented by one.
        :param windowSize: (int, int)
        :return: None
        '''
        self.mouse.position = (30, windowSize[1] / 2 + 10)
        if not self.start_and_stop:
            self.mouse.click(button=self.button, count=1)

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

    # method to check and run loop until
    # it is true another loop will check
    # if it is set to true or not,
    def run(self):
        while self.program_running:
            while self.start_and_stop:
                self.mouse.click(button=self.button, count=1)
                sleep(rb(self.delay - 1, self.delay + 1))
            sleep(0.1)
