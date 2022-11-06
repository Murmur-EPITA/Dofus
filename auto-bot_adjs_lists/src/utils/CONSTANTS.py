from pynput.mouse import Button
from pynput.keyboard import KeyCode, Key

DELAY_CLICK = 6  # seconds
BUTTON = Button.left
BUTTON_POS = KeyCode(char='u')

UP_ARROW = Key.up
RIGHT_ARROW = Key.right
DOWN_ARROW = Key.down
LEFT_ARROW = Key.left

#put None in adjency list
ADD_UP = KeyCode(char='z')
ADD_RIGHT = KeyCode(char='d')
ADD_DOWN = KeyCode(char='s')
ADD_LEFT = KeyCode(char='q')

MOVE_WINDOW = KeyCode(char='i')
START_AND_STOP = KeyCode(char='a')
TERMINATE = KeyCode(char='b')


