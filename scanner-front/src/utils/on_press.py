from pynput.keyboard import Listener, KeyCode

from src.utils.CONSTANTS import START_AND_STOP, TERMINATE
import ClickMouse


def on_press(key: KeyCode, click_thread: ClickMouse):
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


with Listener(on_press=on_press) as listener:
    listener.join()
