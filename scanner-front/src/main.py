from pynput.mouse import Controller
from pynput.keyboard import Listener
from src.HDV.HDV import start_hdv
from src.utils.ClickMouse import ClickMouse
from src.utils.CONSTANTS import *

# launch dofus launcher
# click on hdv


def on_press(key: KeyCode):
    # START_AND_STOP  will stop clicking
    # if running flag is set to true
    if key == START_AND_STOP:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    # here exit method is called and when
    # key is pressed it terminates auto clicker
    elif key == TERMINATE:
        click_thread.exit()
        listener.stop()


if __name__ == '__main__':
    mouse = Controller()
    click_thread = ClickMouse(DELAY_CLICK, BUTTON, mouse)
    click_thread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()

    start_hdv()

