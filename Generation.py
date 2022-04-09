import random
from random import randint

import numpy as np

from Cell import Cell
from Maze import Maze, connect


def _generateFullMaze(width: int, height: int):
    maze = list()
    for i in range(0, height):
        for j in range(0, width):
            maze.append(Cell(x=i, y=j))
    b = np.array(maze).reshape(height, width)
    return Maze(b, (0, 0), width, height)

def depthFirstSearchMaze(n, m):
    maze = _generateFullMaze(n, m)
    maze.start_position = maze.cells[randint(0, maze.width - 1)][maze.height - 1]
    _depthFirstSearch(maze, maze.start_position)
    maze.resetVisited()
    return maze


def _depthFirstSearch(maze: Maze, cell: Cell):
    cell.visited = True
    neigh = maze.getNonVisitedNeighbours(cell)
    while len(neigh) > 0:
        direction = random.choice(list(neigh.keys()))
        connect(cell, neigh[direction], direction)
        _depthFirstSearch(maze, neigh[direction])
        neigh = maze.getNonVisitedNeighbours(cell)
