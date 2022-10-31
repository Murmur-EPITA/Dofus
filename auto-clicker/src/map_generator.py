from src.utils.RESOURCES import *
from src.utils.MAP import dofusMap

def get_adjs(x: int, y: int) -> list[str]:
    """
    adjs is represented this way:
    [DIRECTION.UP, DIRECTION.RIGHT, DIRECTION.DOWN, DIRECTION.LEFT]
    :param x: int
    :param y: int
    :return: list[str]
    """
    posUP = (x, y - 1)
    posRIGHT = (x + 1, y)
    posDOWN = (x, y + 1)
    posLEFT = (x - 1, y)
    pos = [posUP, posRIGHT, posDOWN, posLEFT]
    return list(map(str, pos))


def add_to_hashmap(resourceId: int, nbResources: int, x: int, y: int):
    '''
    Fill 'resources' field from Square objects contained in 'dofusMap'
    :param resourceId: int
    :param nbResources: int
    :param x: int
    :param y: int
    :return: None
    '''
    id = ','.join([str(x), str(y)])
    resource: Resources = 0
    # prefix = ''
    if 1 <= resourceId <= 22:
        resource: Fish = Fish(resourceId)
    elif resourceId == 80 or 23 <= resourceId <= 35:
        resource: Cereal = Cereal(resourceId)
    elif 36 <= resourceId <= 46:
        resource: Flower = Flower(resourceId)
    elif 47 <= resourceId <= 65:
        resource: Wood = Wood(resourceId)
    elif 67 <= resourceId <= 78:
        resource: Ore = Ore(resourceId)
    dofusMap.get(id).resources.append((resource, nbResources))
    print(dofusMap)


def parse_request(response: str):
    tmp = response.split('&')
    resourceId, groupId = int(tmp[0]), int(tmp[1])
    toParse: str = tmp[2]
    byQuantity = toParse.split('_')
    for quantityGroup in byQuantity:
        tmp = quantityGroup.split('*')
        nbResources: int = int(tmp[0])
        quantityGroup2: str = tmp[1]
        groups: list[str] = quantityGroup2.split('+')
        for group in groups:
            tmp = group.split(':')
            x, y = int(tmp[0]), int(tmp[1])
            add_to_hashmap(resourceId, nbResources, x, y)



def generate(x_top_left_corner: int,
             y_top_left_corner: int,
             x_down_right_corner: int,
             y_down_right_corner: int
             ):
    xT, yT, xD, yD = x_top_left_corner, y_top_left_corner, x_down_right_corner, y_down_right_corner
    assert xT <= xD
    assert yT <= yD

    with open("result.txt", "w") as file:
        file.writelines('map = {\n')
        for i in range(xT, xD + 1, 1):
            for j in range(yT, yD + 1, 1):
                x = i
                y = j
                id = ','.join([str(i), str(j)])
                city = "Astrub"
                adjs = get_adjs(x, y)
                string = '\t\'{id}\': Square(id="{id}", x={x}, y={y}, city="{city}", place="",' \
                         ' adjs={adjs}, resources=[], specialSquares=[]),' \
                    .format(id=id, x=x, y=y, city=city, adjs=adjs)
                file.write(string + '\n')
        file.writelines('}')


if __name__ == '__main__':
    # generate(-1, -28, 12, -15)
    add_to_hashmap(61, 5, -1, -28)
