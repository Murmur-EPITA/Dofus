from pygetwindow import Window, getWindowsWithTitle, getAllTitles


def find_dofus_window() -> Window:
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
        self.move()
        self.resize()

    def move(self):
        self.window.moveTo(0, 0)

    def resize(self):
        # width is 1.25x the height
        self.window.resizeTo(1245, 1000)
