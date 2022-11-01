from os.path import exists
from requests import get, Response

from src.utils.DofusMapEnum import DofusMap
from src.utils.MAP import dofusMaps
from src.utils.RESOURCES import *
from src.utils.Square import Square


def get_adjs(x: int, y: int) -> list[str]:
    """
    Get adjacency list of current square.
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


def add_to_hashmap(resourceId: int, groupId: int, nbResources: int, x: int, y: int):
    '''
    Fill 'resources' field from Square objects contained in 'dofusMap'
    :param groupId:
    :param resourceId: int
    :param nbResources: int
    :param x: int
    :param y: int
    :return: None
    '''
    id = ','.join([str(x), str(y)])
    group = DofusMap(groupId)
    resource: Resources = RESOURCES[resourceId]
    square = dofusMaps.get(group.name[:1] + group.name[1:].lower()).get(id)
    if square:
        square.resources.append((resource, nbResources))


def parse_squares(string: str, mapId: int):
    """
    Write in a file all the cases of a map
    :param string: str: 'availableMaps' from response
    :param mapId: int
    :return:
    """
    output = {}
    squareGroups = string.split(' ')
    for squareGroup in squareGroups:
        tmp: list[str] = squareGroup.split(':')
        x: int = int(tmp[0])
        output[x] = []
        Lgroups: list[str] = tmp[1].split(',')
        for Lgroup in Lgroups:
            tmp = Lgroup.split('L')
            i: int = int(tmp[0])
            j: int = i + int(tmp[1]) - 1
            output[x].append((i, j))

    ''' At this point, output looks like { -9: [(-6, -4), (-2, 5)], -5: ... } '''
    mapName = ''
    if mapId == DofusMap.AMAKNIEN:
        mapName = 'Amaknien'
    elif mapId == DofusMap.INCARNAM:
        mapName = 'Incarnam'
    elif mapId == DofusMap.ENUTROSOR:
        mapName = 'Enutrosor'
    elif mapId == DofusMap.SRAMBAD:
        mapName = 'Srambad'
    elif mapId == DofusMap.XELORIUM:
        mapName = 'Xelorium'
    else:
        mapName = 'Ecaflipus'

    with open("maps/empty_{mapName}.py".format(mapName=mapName.lower()), "w") as file:
        file.write("from src.utils.DofusMapEnum import DofusMap\nfrom src.utils.Square import Square\n\n")
        file.write(mapName + ' = {\n')
        for x, l in output.items():
            for tup in l:
                for i in range(tup[0], tup[1] + 1, 1):
                    city = "Astrub"
                    adjs = get_adjs(x, i)
                    square = Square(x, i, DofusMap(mapId), city, "", adjs, [], [])
                    id = ','.join([str(x), str(i)])
                    file.write("\t'" + id + "': " + square.__repr__())
        file.writelines('}')


def parse_map_request(response: dict):
    """
    Parse response from https://dofus-map.com/getGroupData.php?groupId={groupId} and
    fill text files
    :param response: str: response from getGroupData.
    :return:
    """
    squaresToParse: str = response['availableMaps']
    mapId: int = response['id']
    parse_squares(squaresToParse, mapId)
    markersToParse: str = response['markers']


def parse_resources_request(response: str):
    """
    Parse response from https://dofus-map.com/getRessourceData.php?ressourceId={id}&groupId={groupId} and
    add resources to corresponding map's squares.
    :param response: str: response from getResourceData.
    e.g: "44&0&3*-40:-16+-56:25_2*11:15+10:17+9:15 16+-15:39+-14:37 38 39+-13:38+-11:13 18_1*11:16+10:15 16+9:14+8:16 17+12:17+-23:-60+-22:-60+-21:-59 -60+-20:-60+-19:-58+-15:37 38+-13:13 14 37 39+-12:14 16+-11:14+-10:13 16_4*10:14"
    :return:
    """
    tmp = response.split('&')
    resourceId, groupId = int(tmp[0]), int(tmp[1])
    toParse: str = tmp[2]
    if not toParse:
        return
    byQuantity = toParse.split('_')
    for quantityGroup in byQuantity:
        tmp = quantityGroup.split('*')
        nbResources: int = int(tmp[0])
        quantityGroup2: str = tmp[1]
        groups: list[str] = quantityGroup2.split('+')
        for group in groups:
            tmp = group.split(':')
            x: int = int(tmp[0])
            for y in tmp[1].split(' '):
                add_to_hashmap(resourceId, groupId, nbResources, x, int(y))


def generate_maps(maps: list[DofusMap]):
    for dofusMap in maps:
        print('\n' + dofusMap.name + ":", "Fetching map data.")
        mapName = dofusMap.name[:1] + dofusMap.name[1:].lower()
        if not exists("maps/empty_{mapName}.py".format(mapName=mapName.lower())):
            response: Response = get(url="https://dofus-map.com/getGroupData.php?groupId=" + str(dofusMap))
            parse_map_request(response.json())
            print(dofusMap.name + ":", "Empty Map initialized and writtn in 'maps' folder.")
        else:
            print(dofusMap.name + ":", "Empty Map already exists in 'maps' folder.")
        print(dofusMap.name + ":", "Fetching resources data.")

        for key, value in RESOURCES.items():
            response: str = get(url="https://dofus-map.com/getRessourceData.php?ressourceId={id}&groupId={groupId}".format(id=key, groupId=(str(dofusMap)))).text[1:-1]
            parse_resources_request(response)
        print(dofusMap.name + ":", "Filled Map initialized. Writing it to file...")

        with open("maps/{mapName}.py".format(mapName=mapName), "w") as file:
            file.write( "from src.utils.DofusMapEnum import DofusMap\n"
                        "from src.utils.Square import Square\n"
                        "from src.utils.RESOURCES import CEREAL\n"
                        "from src.utils.RESOURCES import FISH\n"
                        "from src.utils.RESOURCES import FLOWER\n"
                        "from src.utils.RESOURCES import RESOURCES\n"
                        "from src.utils.RESOURCES import ORE\n"
                        "from src.utils.RESOURCES import WOOD\n\n")
            file.write(mapName + ' = {\n')
            for key, val in dofusMaps.get(mapName).items():
                file.write("\t'{key}': {val}".format(key=key, val=val.__repr__()))
            file.write('}')
        print(dofusMap.name + ":", "Filled Map written in 'maps' folder.")


if __name__ == '__main__':
    # gen all maps
    generate_maps(list(DofusMap))
    #generate_maps([DofusMap.INCARNAM])
    # print(dofusMaps['Incarnam'])
