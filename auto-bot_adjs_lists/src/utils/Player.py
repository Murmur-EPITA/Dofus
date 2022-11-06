from time import sleep
from src.utils.CONSTANTS import DELAY_CLICK

from src.graph.graph import GraphMap
from src.utils.DIRECTION import Direction
from src.utils.WindowManagement import WindowManagement


class PosX:
    def __init__(self, player, mouse, pos: int):
        self.player = player
        self.mouse = mouse
        self.pos = pos

    def __str__(self):
        return self.pos.__str__()


class PosY:
    def __init__(self, player, mouse, pos: int):
        self.player = player
        self.mouse = mouse
        self.pos = pos

    def __str__(self):
        return self.pos.__str__()


class Player:
    direction: Direction | None = None

    def __init__(self, window: WindowManagement, mouse, graphMap: GraphMap, x, y):
        self.windowManagement = window
        self.mouse = mouse
        self.graph = graphMap
        self.posX = PosX(self, mouse, x)
        self.posY = PosY(self, mouse, y)

    def get_id(self):
        return ','.join([str(self.posX), str(self.posY)])

    def move_to(self, idSquare: str):
        path: list[str] = self.graph.shortest_path(self.get_id(), idSquare)
        x, y = self.posX.pos, self.posY.pos
        for squareId in path:
            xtmp, ytmp = (int(lol) for lol in squareId.split(','))
            if x < xtmp:
                self.mouse.go_right(self.windowManagement.window.size, self)
            elif x > xtmp:
                self.mouse.go_left(self.windowManagement.window.size, self)
            elif y < ytmp:
                self.mouse.go_down(self.windowManagement.window.size, self)
            elif y > ytmp:
                self.mouse.go_up(self.windowManagement.window.size, self)
            # sleep(DELAY_CLICK)
        print("Arrived at pos", self.get_id())


    def __str__(self):
        return "({0},{1})".format(self.posX, self.posY)
