class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.walls = {
            't': True,
            'b': True,
            'l': True,
            'r': True
        }
        self.visited = False

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __str__(self):
        self.walls.keys()
        return f'({self.x}, {self.y})'

    def getWalls(self):
        walls = self.walls
        return list(filter(lambda x: walls[x], walls.keys()))

    def getPassages(self):
        walls = self.walls
        return list(filter(lambda x: not walls[x], walls.keys()))

    def getNeighbours(self):
        walls: list = self.getPassages()
        ans: list = list()
        if walls.__contains__('t'):
            ans.append((self.x, self.y + 1))
        if walls.__contains__('b'):
            ans.append((self.x, self.y - 1))
        if walls.__contains__('l'):
            ans.append((self.x - 1, self.y))
        if walls.__contains__('r'):
            ans.append((self.x + 1, self.y))
        return ans

    def getWall(self, side):
        return self.walls[side]
