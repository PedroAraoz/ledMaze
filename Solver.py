import numpy as np
from numpy import matrix
from typing import List

from Cell import Cell
from Maze import Maze


def adjacentEdges(maze: matrix, cell: Cell):
    b = cell.getNeighbours()
    a = list(map(lambda x: maze[x], b))
    return a


def pop(lst: list):
    e = lst[0]
    lst.remove(e)
    return e


def BFS(maze: Maze):
    start = maze.start_position
    start.visited = True
    queue = list()
    queue.append(start)
    while len(queue) > 0:
        v = pop(queue)
        # win condition
        if v.y == maze.height - 1:
            return v
        neighbors: List[Cell] = adjacentEdges(maze.cells, v)
        for n in neighbors:
            print("NO!!!!")
            n.visited = True
            #       neighbors[i].parent = curNode;
            queue.append(n)
