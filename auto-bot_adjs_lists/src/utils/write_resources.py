# format:
# adjs = {
#   {'5,-74': [UP, RIGHT, DOWN, LEFT]},
#   {'9,-7': [(2, -98), (...), DOWN, LEFT]}
# }

adjs = {

}


def get_adjs(x: int, y: int):
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


def write_dict_all(dico: dict):
    with open('../adjs.py', 'w') as file:
        file.write('adjs = {\n')
        for key, value in dico.items():
            string = "\t{ '{key}': [{value1}, {value2}, {value3}, {value4}] }\n".format(key=key, value1=value[0],
                                                                                        value2=value[1],
                                                                                        value3=value[2],
                                                                                        value4=value[3])
            file.write(string)
        file.write('}')
