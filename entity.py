class Entity:
    """
    A generic entity object. Entities are anything that is interact-able that isn't the map itself.

    Examples: Players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color, name):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
