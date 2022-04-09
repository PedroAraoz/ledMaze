class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.walls = {
            'north': True,
            'south': True,
            'east': True,
            'west': True
        }
        self.visited = False

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        self.walls.keys()
        return f'({self.x}, {self.y})'

    def connect(self, direction):
        self.walls[direction] = False
