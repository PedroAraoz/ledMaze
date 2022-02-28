from Cell import Cell
from Maze import Maze
import numpy as np


def generateFullMaze(width: int, height: int):
    maze = list()
    for i in range(0, height):
        for j in range(0, width):
            maze.append(Cell(x=i, y=j))
    b = np.array(maze).reshape(height, width)
    return Maze(b, (0, 0), width, height)
