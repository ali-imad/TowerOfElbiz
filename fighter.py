from entity import Entity
import numpy as np


class Fighter(Entity):
    def __init__(self, x, y, char, colour, name):
        Entity.__init__(self, x, y, char, colour, name)
