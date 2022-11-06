def getPercent(percentage, total, integer=False):
    percent = percentage * total / 100

    if integer:
        return int(percent)
    return percent


import random


def random_between(min, max):
    return random.uniform(min, max)

def random_almost(val, distance=300):
    return random_between(val - distance, val + distance)
