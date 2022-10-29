from pynput.mouse import Controller
from pynput.keyboard import Listener
from src.utils.ClickMouse import ClickMouse
from src.utils.CONSTANTS import *
from src.utils.WindowManagement import WindowManagement


class Main:
    def __init__(self):
        def on_press(key: KeyCode | Key):
            # START_AND_STOP  will stop clicking
            # if running flag is set to true

            if key == START_AND_STOP:
                if self.click_thread.running:
                    self.click_thread.stop_clicking()
                else:
                    self.click_thread.start_clicking()

            elif key == UP_ARROW:
                self.click_thread.go_up()

            elif key == RIGHT_ARROW:
                self.click_thread.go_right()

            elif key == DOWN_ARROW:
                self.click_thread.go_down()

            elif key == LEFT_ARROW:
                self.click_thread.go_left()

            # here exit method is called and when
            # key is pressed it terminates auto clickerb
            elif key == TERMINATE:
                self.click_thread.exit()
                listener.stop()

        windowManagement = WindowManagement()

        self.mouse = Controller()
        self.click_thread = ClickMouse(DELAY_CLICK, BUTTON, self.mouse)
        self.click_thread.start()

        with Listener(on_press=on_press) as listener:
            listener.join()


if __name__ == '__main__':
    instance = Main()
