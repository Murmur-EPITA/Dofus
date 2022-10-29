from pynput.mouse import Controller
from pynput.keyboard import Listener
from src.utils.ClickMouse import ClickMouse
from src.utils.CONSTANTS import *


class Main:
    def __init__(self):
        def on_press(key: KeyCode):
            # START_AND_STOP  will stop clicking
            # if running flag is set to true
            if key == START_AND_STOP:
                if self.click_thread.running:
                    self.click_thread.stop_clicking()
                else:
                    self.click_thread.start_clicking()

            # here exit method is called and when
            # key is pressed it terminates auto clicker
            elif key == TERMINATE:
                self.click_thread.exit()
                listener.stop()

        self.mouse = Controller()
        self.click_thread = ClickMouse(DELAY_CLICK, BUTTON, self.mouse)
        self.click_thread.start()

        with Listener(on_press=on_press) as listener:
            listener.join()


def go_left():
    pass


if __name__ == '__main__':
    instance = Main()
