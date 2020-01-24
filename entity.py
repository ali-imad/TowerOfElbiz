class Entity:
    """
    A generic entity object. Entities are anything that is interactable that isnt the map itself.

    Examples: Players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy):
        """
        Moves the entity to (x+dx, y+dy)
        """
        self.x += dx
        self.y += dy
