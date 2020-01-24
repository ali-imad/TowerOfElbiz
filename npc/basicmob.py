from entity import Entity

class BasicMob(Entity):
    def __init__(self, x, y, char, color, mob_type):
        Entity.__init__(x, y, char, color)
        BasicMob.mob_type = mob_type

    def path(self, target):
        """
        Determine where to go based on where the target is.
        :return:
        """
        pass
