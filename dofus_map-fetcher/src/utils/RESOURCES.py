from enum import IntEnum


class Resources:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FISH(IntEnum):
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


class Fish(Resources):
    def __repr__(self):
        return "RESOURCES[FISH.{enum}]".format(enum=FISH(self.id).name)


class CEREAL(IntEnum):
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


class Cereal(Resources):
    def __repr__(self):
        return "RESOURCES[CEREAL.{enum}]".format(enum=CEREAL(self.id).name)


class FLOWER(IntEnum):
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


class Flower(Resources):
    def __repr__(self):
        return "RESOURCES[FLOWER.{enum}]".format(enum=FLOWER(self.id).name)


class WOOD(IntEnum):
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


class Wood(Resources):
    def __repr__(self):
        return "RESOURCES[WOOD.{enum}]".format(enum=WOOD(self.id).name)


class ORE(IntEnum):
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


class Ore(Resources):
    def __repr__(self):
        return "RESOURCES[ORE.{enum}]".format(enum=ORE(self.id).name)


'''
int: (Resources(int, str))
'''
RESOURCES = {
    FISH.GOUJON: Fish(FISH.GOUJON.value, FISH.GOUJON.name.lower()),
    FISH.GREUVETTE: Fish(FISH.GREUVETTE.value, FISH.GREUVETTE.name.lower()),
    FISH.TRUITE: Fish(FISH.TRUITE.value, FISH.TRUITE.name.lower()),
    FISH.CRABE: Fish(FISH.CRABE.value, FISH.CRABE.name.lower()),
    FISH.POISSONCHATON: Fish(FISH.POISSONCHATON.value, FISH.POISSONCHATON.name.lower()),
    FISH.POISSONPANE: Fish(FISH.POISSONPANE.value, FISH.POISSONPANE.name.lower()),
    FISH.CARPEDIEM: Fish(FISH.CARPEDIEM.value, FISH.CARPEDIEM.name.lower()),
    FISH.SARDINE: Fish(FISH.SARDINE.value, FISH.SARDINE.name.lower()),
    FISH.BROCHET: Fish(FISH.BROCHET.value, FISH.BROCHET.name.lower()),
    FISH.KRALAMOURE: Fish(FISH.KRALAMOURE.value, FISH.KRALAMOURE.name.lower()),
    FISH.ANGUILLE: Fish(FISH.ANGUILLE.value, FISH.ANGUILLE.name.lower()),
    FISH.DORADE: Fish(FISH.DORADE.value, FISH.DORADE.name.lower()),
    FISH.PERCHE: Fish(FISH.PERCHE.value, FISH.PERCHE.name.lower()),
    FISH.RAIE: Fish(FISH.RAIE.value, FISH.RAIE.name.lower()),
    FISH.LOTTE: Fish(FISH.LOTTE.value, FISH.LOTTE.name.lower()),
    FISH.REQUIN: Fish(FISH.REQUIN.value, FISH.REQUIN.name.lower()),
    FISH.BAR: Fish(FISH.BAR.value, FISH.BAR.name.lower()),
    FISH.MORUE: Fish(FISH.MORUE.value, FISH.MORUE.name.lower()),
    FISH.TANCHE: Fish(FISH.TANCHE.value, FISH.TANCHE.name.lower()),
    FISH.ESPADON: Fish(FISH.ESPADON.value, FISH.ESPADON.name.lower()),
    FISH.POISSKAILLE: Fish(FISH.POISSKAILLE.value, FISH.POISSKAILLE.name.lower()),
    FISH.PATELLE: Fish(FISH.PATELLE.value, FISH.PATELLE.name.lower()),

    CEREAL.BLE: Cereal(CEREAL.BLE.value, CEREAL.BLE.name.lower()),
    CEREAL.ORGE: Cereal(CEREAL.ORGE.value, CEREAL.ORGE.name.lower()),
    CEREAL.AVOINE: Cereal(CEREAL.AVOINE.value, CEREAL.AVOINE.name.lower()),
    CEREAL.HOUBLON: Cereal(CEREAL.HOUBLON.value, CEREAL.HOUBLON.name.lower()),
    CEREAL.LIN: Cereal(CEREAL.LIN.value, CEREAL.LIN.name.lower()),
    CEREAL.SEIGLE: Cereal(CEREAL.SEIGLE.value, CEREAL.SEIGLE.name.lower()),
    CEREAL.RIZ: Cereal(CEREAL.RIZ.value, CEREAL.RIZ.name.lower()),
    CEREAL.MALT: Cereal(CEREAL.MALT.value, CEREAL.MALT.name.lower()),
    CEREAL.CHANVRE: Cereal(CEREAL.CHANVRE.value, CEREAL.CHANVRE.name.lower()),
    CEREAL.MAIS: Cereal(CEREAL.MAIS.value, CEREAL.MAIS.name.lower()),
    CEREAL.MILLET: Cereal(CEREAL.MILLET.value, CEREAL.MILLET.name.lower()),
    CEREAL.FROSTIZ: Cereal(CEREAL.FROSTIZ.value, CEREAL.FROSTIZ.name.lower()),
    CEREAL.QUISNOA: Cereal(CEREAL.QUISNOA.value, CEREAL.QUISNOA.name.lower()),

    FLOWER.ORTIE: Flower(FLOWER.ORTIE.value, FLOWER.ORTIE.name.lower()),
    FLOWER.SAUGE: Flower(FLOWER.SAUGE.value, FLOWER.SAUGE.name.lower()),
    FLOWER.TREFLE: Flower(FLOWER.TREFLE.value, FLOWER.TREFLE.name.lower()),
    FLOWER.MENTHE: Flower(FLOWER.MENTHE.value, FLOWER.MENTHE.name.lower()),
    FLOWER.ORCHIDEE: Flower(FLOWER.ORCHIDEE.value, FLOWER.ORCHIDEE.name.lower()),
    FLOWER.EDELWEISS: Flower(FLOWER.EDELWEISS.value, FLOWER.EDELWEISS.name.lower()),
    FLOWER.PANDOUILLE: Flower(FLOWER.PANDOUILLE.value, FLOWER.PANDOUILLE.name.lower()),
    FLOWER.GINSENG: Flower(FLOWER.GINSENG.value, FLOWER.GINSENG.name.lower()),
    FLOWER.BELLADONE: Flower(FLOWER.BELLADONE.value, FLOWER.BELLADONE.name.lower()),
    FLOWER.MANDRAGORE: Flower(FLOWER.MANDRAGORE.value, FLOWER.MANDRAGORE.name.lower()),
    FLOWER.PERCENEIGE: Flower(FLOWER.PERCENEIGE.value, FLOWER.PERCENEIGE.name.lower()),
    FLOWER.SALIKRONE: Flower(FLOWER.SALIKRONE.value, FLOWER.SALIKRONE.name.lower()),

    WOOD.FRENE: Wood(WOOD.FRENE.value, WOOD.FRENE.name.lower()),
    WOOD.CHATAIGNIER: Wood(WOOD.CHATAIGNIER.value, WOOD.CHATAIGNIER.name.lower()),
    WOOD.NOYER: Wood(WOOD.NOYER.value, WOOD.NOYER.name.lower()),
    WOOD.CHENE: Wood(WOOD.CHENE.value, WOOD.CHENE.name.lower()),
    WOOD.BOMBU: Wood(WOOD.BOMBU.value, WOOD.BOMBU.name.lower()),
    WOOD.ERABLE: Wood(WOOD.ERABLE.value, WOOD.ERABLE.name.lower()),
    WOOD.OLIVIOLET: Wood(WOOD.OLIVIOLET.value, WOOD.OLIVIOLET.name.lower()),
    WOOD.IF: Wood(WOOD.IF.value, WOOD.IF.name.lower()),
    WOOD.BAMBOU: Wood(WOOD.BAMBOU.value, WOOD.BAMBOU.name.lower()),
    WOOD.MERISIER: Wood(WOOD.MERISIER.value, WOOD.MERISIER.name.lower()),
    WOOD.NOISETIER: Wood(WOOD.NOISETIER.value, WOOD.NOISETIER.name.lower()),
    WOOD.EBENE: Wood(WOOD.EBENE.value, WOOD.EBENE.name.lower()),
    WOOD.KALIPTUS: Wood(WOOD.KALIPTUS.value, WOOD.KALIPTUS.name.lower()),
    WOOD.CHARME: Wood(WOOD.CHARME.value, WOOD.CHARME.name.lower()),
    WOOD.BAMBOUSOMBRE: Wood(WOOD.BAMBOUSOMBRE.value, WOOD.BAMBOUSOMBRE.name.lower()),
    WOOD.ORME: Wood(WOOD.ORME.value, WOOD.ORME.name.lower()),
    WOOD.BAMBOUSACRE: Wood(WOOD.BAMBOUSACRE.value, WOOD.BAMBOUSACRE.name.lower()),
    WOOD.TREMBLE: Wood(WOOD.TREMBLE.value, WOOD.TREMBLE.name.lower()),
    WOOD.AQUAJOU: Wood(WOOD.AQUAJOU.value, WOOD.AQUAJOU.name.lower()),

    ORE.CUIVRE: Ore(ORE.CUIVRE.value, ORE.CUIVRE.name.lower()),
    ORE.FER: Ore(ORE.FER.value, ORE.FER.name.lower()),
    ORE.BRONZE: Ore(ORE.BRONZE.value, ORE.BRONZE.name.lower()),
    ORE.KOBALTE: Ore(ORE.KOBALTE.value, ORE.KOBALTE.name.lower()),
    ORE.MANGANESE: Ore(ORE.MANGANESE.value, ORE.MANGANESE.name.lower()),
    ORE.ETAIN: Ore(ORE.ETAIN.value, ORE.ETAIN.name.lower()),
    ORE.SILICATE: Ore(ORE.SILICATE.value, ORE.SILICATE.name.lower()),
    ORE.ARGENT: Ore(ORE.ARGENT.value, ORE.ARGENT.name.lower()),
    ORE.BAUXITE: Ore(ORE.BAUXITE.value, ORE.BAUXITE.name.lower()),
    ORE.OR: Ore(ORE.OR.value, ORE.OR.name.lower()),
    ORE.DOLOMITE: Ore(ORE.DOLOMITE.value, ORE.DOLOMITE.name.lower()),
    ORE.OBSIDIENNE: Ore(ORE.OBSIDIENNE.value, ORE.OBSIDIENNE.name.lower())
}
