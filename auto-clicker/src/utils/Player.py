from src.utils.ClickMouse import ClickMouse
from src.utils.WindowManagement import WindowManagement


class PosX:
    def __init__(self, player, mouse: ClickMouse, pos: int):
        self.player = player
        self.mouse = mouse
        self.pos = pos

    def __eq__(self, other: int):
        return self.pos == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iadd__(self, other: int):
        self.mouse.go_right(self.player.windowManagement.window.size)
        self.player.posX.pos += 1

    def __isub__(self, other: int):
        self.mouse.go_left(self.player.windowManagement.window.size)
        self.player.posX.pos -= 1

    def __str__(self):
        return self.pos.__str__()


class PosY:
    def __init__(self, player, mouse: ClickMouse, pos: int):
        self.player = player
        self.mouse = mouse
        self.pos = pos

    def __eq__(self, other: int):
        return self.pos == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __iadd__(self, other: int):
        self.mouse.go_down(self.player.windowManagement.window.size)
        self.player.posY.pos += 1

    def __isub__(self, other: int):
        self.mouse.go_up(self.player.windowManagement.window.size)
        self.player.posY.pos -= 1

    def __str__(self):
        return self.pos.__str__()


class Player:
    def __init__(self, window: WindowManagement, mouse: ClickMouse, x, y):
        self.windowManagement = window
        self.mouse = mouse
        self.posX = PosX(self, mouse, x)
        self.posY = PosY(self, mouse, y)

    def __str__(self):
        return "({0},{1})".format(self.posX.pos, self.posY.pos)
