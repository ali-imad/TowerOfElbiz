class Tile:
    """
    A tile on a map. Should mask the GameMap tiles arrays perfectly. Adds additional functionality
    """

    def __init__(self):
        self.explored = False

    def explore(self):
        self.explored = True