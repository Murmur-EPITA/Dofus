from collections import deque
from pynput.keyboard import Listener
from pynput.mouse import Controller
from time import sleep

from src.utils.CONSTANTS import *
from src.utils.ClickMouse import ClickMouse
from src.utils.Player import Player
from src.utils.WindowManagement import WindowManagement
from src.utils.tKinter import ask_pos

global x, y


class Main:
    def __init__(self):
        def on_press(key: KeyCode | Key):
            # START_AND_STOP  will stop clicking
            # if running flag is set to true

            if key == START_AND_STOP:
                if self.click_thread.start_and_stop:
                    self.click_thread.stop_clicking()
                else:
                    self.click_thread.start_clicking()

            elif key == UP_ARROW:
                self.click_thread.go_up(self.windowManagement.window.size)

            elif key == RIGHT_ARROW:
                self.click_thread.go_right(self.windowManagement.window.size)

            elif key == DOWN_ARROW:
                self.click_thread.go_down(self.windowManagement.window.size)

            elif key == LEFT_ARROW:
                self.click_thread.go_left(self.windowManagement.window.size)

            elif key == BUTTON_POS:
                self.player.posX.pos, self.player.posY.pos = ask_pos()

            # here exit method is called and when
            # key is pressed it terminates auto clicker
            elif key == TERMINATE:
                self.click_thread.exit()
                listener.stop()

        self.windowManagement = WindowManagement()
        sleep(2)
        x, y = ask_pos()
        queue = deque()

        self.mouse = Controller()
        self.click_thread = ClickMouse(self.mouse, queue)
        self.click_thread.start()

        self.player = Player(self.windowManagement, self.click_thread, x, y)

        with Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    instance = Main()
