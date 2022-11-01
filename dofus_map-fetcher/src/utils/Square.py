from src.utils.DofusMapEnum import DofusMap
from src.utils.RESOURCES import Cereal as C
from src.utils.RESOURCES import Fish as Fi
from src.utils.RESOURCES import Flower as Fl
from src.utils.RESOURCES import Ore as O
from src.utils.RESOURCES import Resources
from src.utils.RESOURCES import Wood as W

class SpecialSquare:
    pass


class Square:
    '''
    Represent a single square from the huge Dofus map.
        adjs is represented this way:
        [DIRECTION.UP, DIRECTION.RIGHT, DIRECTION.DOWN, DIRECTION.LEFT]

        specialSquares are sub-worlds such as mines etc.
    '''

    def __init__(self,
                 x: int,
                 y: int,
                 dofusMap: int,
                 city: str,
                 place: str,
                 adjs: list[str],
                 resources: list[tuple[Resources, int]],
                 specialSquares: list[SpecialSquare]
                 ):
        self.x = x
        self.y = y
        self.map = dofusMap
        self.city = city
        self.place = place
        self.adjs = adjs
        self.resources = resources
        self.specialSquares = specialSquares

    def __repr__(self):
        prefix = "DofusMap."
        return 'Square(x={x}, y={y}, dofusMap={prefix}{map}, city="{city}", place="",' \
               ' adjs={adjs}, resources={resources}, specialSquares=[]),\n' \
            .format(x=self.x, y=self.y, prefix=prefix,
                    map=DofusMap.AMAKNIEN.name if self.map == 0 else
                    DofusMap.INCARNAM.name if self.map == 1 else
                    DofusMap.ENUTROSOR.name if self.map == 2 else
                    DofusMap.SRAMBAD.name if self.map == 3 else
                    DofusMap.XELORIUM.name if self.map == 4 else
                    DofusMap.ECAFLIPUS.name,
                    city=self.city, adjs=self.adjs,
                    resources=[(resource, nb) for (resource, nb) in self.resources])
