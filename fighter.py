import tcod
from entity import Entity


class Fighter(Entity):
    def __init__(self, x, y, char='@', colour=tcod.white, name='Player'):
        Entity.__init__(self, x, y, char, colour, name)
        self.hp = 16
        self.ap = 3
        self.calc_stats()

    def calc_stats(self):
        """
        Based on name, sets hp and ap (attack power)
        :return:
        """

        if self.name == 'orc':
            self.hp = 8
            self.ap = 2
            self.char = 'o'
            self.color = tcod.darker_red

        if self.name == 'jackal':
            self.hp = 5
            self.ap = 3
            self.char = 'j'
            self.color = tcod.darker_azure

    def move(self, dx, dy):
        """
        moves player.x, player.y by dx and dy, respectively
        :param dx:
        :param dy:
        """
        self.x += dx
        self.y += dy

    def attack(self, other):
        """
        :param other: Fighter
        """
        other.hp -= self.ap
        print("{0} attacked {1}, dealing {2} damage. {1}'s hp is now {3}".format(self.name, other.name, self.ap,
                                                                                 other.hp))

    def move_or_attack(self, dx, dy, game_map):
        """
        TODO: fill in docstring
        TODO: fix the "is not Fighter" check to check the type of entity and act accordingly
        """
        game_map.tiles.contains[self.y, self.x] = None  # reset the "tiles.contains" array in game map in case we move

        if game_map.tiles.walkable[self.y + dy, self.x + dx]:
            if type(game_map.tiles.contains[self.y + dy, self.x + dx]) is not Fighter:  # if there's no fighter
                self.move(dx, dy)
            else:  # game_map.tiles.contains at the location we're heading to has a fighter
                other = game_map.tiles.contains[self.y + dy, self.x + dx]
                self.attack(other)

        game_map.tiles.contains[self.y, self.x] = self  # set the "tiles.contains" array to have

        # debugging only
        print("{0}, {1}".format(self.x, self.y))
