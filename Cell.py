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
        self.step = 0
        self.parent = None

    def connect(self, direction):
        self.walls[direction] = False

