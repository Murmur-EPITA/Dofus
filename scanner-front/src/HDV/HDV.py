from src.utils.CONSTANTS import DELAY_CLICK, BUTTON
from src.utils.ClickMouse import *


def start_hdv(mouse: Controller):
    print('start_hdv')
    click_thread = ClickMouse(DELAY_CLICK, BUTTON, mouse)
    click_thread.start()
