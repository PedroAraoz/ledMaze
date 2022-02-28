import random
from random import randint
from time import sleep

import numpy as np
from matplotlib import patches
from matplotlib.path import Path

from Cell import Cell
from Maze import Maze


def draw(maze: Maze, plt):
    rect = patches.Rectangle((0, 0), 8, 8, linewidth=6, edgecolor='r', facecolor='none')

    fig, ax = plt.subplots()
    ax.set(autoscale_on=False, xlim=(0, 8), ylim=(0, 9))
    np.vectorize(drawCell)(maze.cells, ax)
    x, _ = maze.start_position.coords
    ax.annotate("", xy=(x + .5, 8), xytext=(x + .5, 9), arrowprops=dict(arrowstyle="->"))
    ax.add_patch(rect)


def top(cell: Cell):
    x, y = cell.coords
    path = Path([(x, y + 1), (x + 1, y + 1)], [Path.MOVETO, Path.LINETO])
    return patches.PathPatch(path, facecolor='none', lw=2)


def bottom(cell: Cell):
    x, y = cell.coords
    path = Path([(x, y), (x + 1, y)], [Path.MOVETO, Path.LINETO])
    return patches.PathPatch(path, facecolor='none', lw=2)


def right(cell: Cell):
    x, y = cell.coords
    path = Path([(x + 1, y), (x + 1, y + 1)], [Path.MOVETO, Path.LINETO])
    return patches.PathPatch(path, facecolor='none', lw=2)


def left(cell: Cell):
    x, y = cell.coords
    path = Path([(x, y), (x, y + 1)], [Path.MOVETO, Path.LINETO])
    return patches.PathPatch(path, facecolor='none', lw=2)


def drawCell(cell: Cell, ax):
    if cell.visited:
        ax.plot(cell.x + 0.5, cell.y + 0.5, "ro")
    if cell.walls['t']:
        ax.add_patch(top(cell))
    if cell.walls['b']:
        ax.add_patch(bottom(cell))
    if cell.walls['r']:
        ax.add_patch(right(cell))
    if cell.walls['l']:
        ax.add_patch(left(cell))
