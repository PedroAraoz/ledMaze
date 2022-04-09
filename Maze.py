from numpy import matrix

import Cell


def connect(c1, c2, direction):
    oposite = {
        'west': 'east',
        'east': 'west',
        'north': 'south',
        'south': 'north'
    }
    c1.connect(direction)
    c2.connect(oposite[direction])


class Maze:
    def __init__(self, cells: matrix, start_position, width, height):
        self.cells = cells
        self.start_position = cells[start_position]
        self.width, self.height = width, height
        self.dimension = (width, height)

    def resetVisited(self):
        for line in self.cells:
            for c in line:
                c.visited = False

    def getNeighbours(self, cell: Cell):
        (x, y) = cell.coords
        neigh = dict()
        if y + 1 < self.height:
            neigh['north'] = self.cells[x, y + 1]
        if y - 1 >= 0:
            neigh['south'] = self.cells[x, y - 1]
        if x - 1 >= 0:
            neigh['west'] = self.cells[x - 1, y]
        if x + 1 < self.width:
            neigh['east'] = self.cells[x + 1, y]
        return neigh

    def getNonVisitedNeighbours(self, cell: Cell):
        neigh = self.getNeighbours(cell)
        return {k: v for (k, v) in neigh.items() if not v.visited}

    def getNeighboursSorted(self, cell: Cell):
        neigh = self.getNeighbours(cell)
        key_order = ['east', 'west', 'south', 'north']
        return {k: neigh[k] for k in key_order if k in neigh}
