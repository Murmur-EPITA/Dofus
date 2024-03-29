from pynput.mouse import Controller
from threading import Thread

from src.utils.CONSTANTS import *
from src.utils.DIRECTION import *
from src.utils.other import getPercent, random_almost
from src.utils.Player import Player


class ClickMouse(Thread):
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, mouse: Controller):
        super(ClickMouse, self).__init__()
        self.button = Button(BUTTON)
        self.program_running = True
        self.mouse = mouse
        print('ClickMouse created.')

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
        previous: Direction = player.direction
        player.direction = Direction.UP
        if previous is not None and previous == 0:
            player.posY.pos -= 1
            self.mouse.click(button=self.button, count=1)
            player.direction = None
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
        previous: Direction = player.direction
        player.direction = Direction.RIGHT
        if previous and previous == Direction.RIGHT:
            player.posX.pos += 1
            self.mouse.click(button=self.button, count=1)
            player.direction = None
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
        previous: Direction = player.direction
        player.direction = Direction.DOWN
        if previous and previous == Direction.DOWN:
            player.posY.pos += 1
            self.mouse.click(button=self.button, count=1)
            player.direction = None
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
        previous: Direction = player.direction
        player.direction = Direction.LEFT
        if previous and previous == Direction.LEFT:
            player.posX.pos -= 1
            self.mouse.click(button=self.button, count=1)
            player.direction = None
            self.mouse.position = (windowSize[0] / 2, windowSize[1] / 2)
