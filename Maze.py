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
    def __init__(self, cells, start_position, width, height):
        self.cells = cells
        self.start_position = cells[start_position[0]][start_position[1]]
        self.end_position = None
        self.width, self.height = width, height
        self.dimension = (width, height)
        self.totalSteps = -1

    def reset_visited(self):
        for line in self.cells:
            for c in line:
                c.visited = False

    def get_neighbours(self, cell: Cell):
        (x, y) = cell.coords
        neigh = dict()
        if y + 1 < self.height:
            neigh['north'] = self.cells[x][y + 1]
        if y - 1 >= 0:
            neigh['south'] = self.cells[x][y - 1]
        if x - 1 >= 0:
            neigh['west'] = self.cells[x - 1][y]
        if x + 1 < self.width:
            neigh['east'] = self.cells[x + 1][y]
        return neigh

    def get_non_visited_neighbours(self, cell: Cell):
        neigh = self.get_neighbours(cell)
        return {k: v for (k, v) in neigh.items() if not v.visited}

    def get_valid_non_visited_neighbours(self, cell: Cell):
        neigh = self.get_non_visited_neighbours(cell)
        a = [k for k, v in cell.walls.items() if not v]
        res = [(k, v) for k, v in neigh.items() if k in a]
        return dict(res)

    def set_end_position(self, cell: Cell):
        self.totalSteps = cell.step
        self.end_position = cell
