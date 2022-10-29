import random
import threading
import time

from pynput.mouse import Controller


class ClickMouse(threading.Thread):
    # delay and button is passed in class
    # to check execution of auto-clicker
    def __init__(self, delay: float, button, mouse: Controller):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True
        self.mouse = mouse
        print('ClickMouse created')

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # method to check and run loop until
    # it is true another loop will check
    # if it is set to true or not,
    # for mouse click it set to button
    # and delay.
    def run(self):
        print('Click Controller initialized.')
        while self.program_running:
            while self.running:
                self.mouse.click(button=self.button, count=1)
                time.sleep(random.uniform(self.delay - 1, self.delay + 1))
            time.sleep(0.1)
