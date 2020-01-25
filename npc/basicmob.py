from fighter import Fighter


class BasicMob(Fighter):
    def __init__(self, x, y, char, color, mob_type):
        Fighter.__init__(x, y, char, color, mob_type)
        self.target = None  # stores the current target at hand

    def path(self, target):
        """
        Determine where to go based on where the target is.
        :return:
        """
        pass
