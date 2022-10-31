from enum import IntEnum


class Resources(IntEnum):
    pass


class Fish(Resources):
    GOUJON = 1
    GREUVETTE = 2
    TRUITE = 3
    CRABE = 4
    POISSONCHATON = 5
    POISSONPANE = 6
    CARPEDIEM = 7
    SARDINE = 8
    BROCHET = 9
    KRALAMOURE = 10
    ANGUILLE = 11
    DORADE = 12
    PERCHE = 13
    RAIE = 14
    LOTTE = 15
    REQUIN = 16
    BAR = 17
    MORUE = 18
    TANCHE = 19
    ESPADON = 20
    POISSKAILLE = 21
    PATELLE = 22


class Cereal(Resources):
    BLE = 23
    ORGE = 24
    AVOINE = 25
    HOUBLON = 26
    LIN = 27
    SEIGLE = 28
    RIZ = 29
    MALT = 30
    CHANVRE = 31
    MAIS = 32
    MILLET = 33
    FROSTIZ = 34
    QUISNOA = 35


class Flower(Resources):
    ORTIE = 36
    SAUGE = 37
    TREFLE = 38
    MENTHE = 39
    ORCHIDEE = 40
    EDELWEISS = 80
    PANDOUILLE = 41
    GINSENG = 42
    BELLADONE = 43
    MANDRAGORE = 44
    PERCENEIGE = 45
    SALIKRONE = 46


class Wood(Resources):
    FRENE = 47
    CHATAIGNIER = 48
    NOYER = 49
    CHENE = 50
    BOMBU = 51
    ERABLE = 52
    OLIVIOLET = 53
    IF = 54
    BAMBOU = 55
    MERISIER = 56
    NOISETIER = 57
    EBENE = 58
    KALIPTUS = 59
    CHARME = 60
    BAMBOUSOMBRE = 61
    ORME = 62
    BAMBOUSACRE = 63
    TREMBLE = 64
    AQUAJOU = 65
    # SCEAU = 66


class Ore(Resources):
    CUIVRE = 67
    FER = 68
    BRONZE = 69
    KOBALTE = 70
    MANGANESE = 71
    ETAIN = 72
    SILICATE = 73
    ARGENT = 74
    BAUXITE = 75
    OR = 76
    DOLOMITE = 77
    OBSIDIENNE = 78
