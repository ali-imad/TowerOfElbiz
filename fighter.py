from entity import Entity


class Fighter(Entity):
    def __init__(self, x, y, char, colour, name):
        Entity.__init__(self, x, y, char, colour, name)

    def move(self, dx, dy):
        """
        Moves the entity to (x+dx, y+dy)
        """
        self.x += dx
        self.y += dy
        # debugging only
        print("{0}, {1}".format(self.x, self.y))
