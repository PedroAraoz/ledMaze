from numpy import matrix


class Maze:
    def __init__(self, cells: matrix, start_position, width, height):
        self.cells = cells
        self.start_position = cells[start_position]
        self.width, self.height = width, height
        self.dimension = (width, height)
