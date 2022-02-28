from random import random, randint

import numpy as np
from numpy import matrix

from Maze import Maze


def singleRandomCarve(cell, y_prob=0.25, x_prob=0.25):
    a, b, c, d = random(), random(), random(), random()
    # cell.walls['t'] = a < y_prob
    # cell.walls['b'] = b < y_prob
    # cell.walls['r'] = c < x_prob
    # cell.walls['l'] = d < x_prob
    return cell


def randomCarve(maze: Maze):
    maze.cells = np.vectorize(singleRandomCarve)(maze.cells)
    maze.start_position = maze.cells[randint(0, maze.width - 1)][0]
    return maze


def depthFirstSearchCarve(maze: Maze):
    return maze

# Given a current cell as a parameter,
# Mark the current cell as visited
# While the current cell has any unvisited neighbour cells
# Choose one of the unvisited neighbours
# Remove the wall between the current cell and the chosen cell
# Invoke the routine recursively for a chosen cell
# which is invoked once for any initial cell in the area.
