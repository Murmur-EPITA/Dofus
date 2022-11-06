from src.utils.DIRECTION import Direction
from src.utils.WindowManagement import WindowManagement


class PosX:
    def __init__(self, player, mouse, pos: int):
        self.player = player
        self.mouse = mouse
        self.pos = pos

    def __iadd__(self, other: int):
        # self.mouse.go_right(self.player.windowManagement.window.size)
        return self.player.posX.pos + other

    def __isub__(self, other: int):
        # self.mouse.go_left(self.player.windowManagement.window.size)
        return self.player.posX.pos - other

    def __str__(self):
        return self.pos.__str__()


class PosY:
    def __init__(self, player, mouse, pos: int):
        self.player = player
        self.mouse = mouse
        self.pos = pos

    def __iadd__(self, other: int):
        # self.mouse.go_down(self.player.windowManagement.window.size)
        return self.player.posY.pos + other

    def __isub__(self, other: int):
        # self.mouse.go_up(self.player.windowManagement.window.size)
        return self.player.posY.pos - other

    def __str__(self):
        return self.pos.__str__()


class Player:
    direction: Direction | None = None
    def __init__(self, window: WindowManagement, mouse, x, y):
        self.windowManagement = window
        self.mouse = mouse
        self.posX = PosX(self, mouse, x)
        self.posY = PosY(self, mouse, y)

    def get_id(self):
        return ','.join([str(self.posX), str(self.posY)])

    def __str__(self):
        return "({0},{1})".format(self.posX, self.posY)
