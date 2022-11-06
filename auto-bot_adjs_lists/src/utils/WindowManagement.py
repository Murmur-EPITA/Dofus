from time import sleep

from pyautogui import getWindowsWithTitle, Window, getAllTitles


def find_dofus_window() -> Window:
    '''
    Look in current windows for the Dofus one thanks to its title.
    :return: dofusWindow :Window
    '''
    titles = getAllTitles()
    title = None
    for tmp_title in titles:
        if "- Dofus 2" in tmp_title:
            title = tmp_title
            break
    print('"', title, '" has been found.')
    return getWindowsWithTitle(title)[0]


class WindowManagement:
    def __init__(self):
        self.window = find_dofus_window()
        self.window.minimize()
        self.window.restore()
        self.window.activate()
        self.resize()
        self.move()
        self.resize()

    def move(self):
        self.window.moveTo(0, 0)

    def resize(self):
        # width is 1.25x the height
        # self.window.resizeTo(1245, 1000)
        self.window.resizeTo(1800, 1200)
        self.window.resize(1, 1)
