import random
from random import randint

from Cell import Cell
from Maze import Maze, connect


def generate_depth_first_search_maze(n, m):
    maze = _generate_full_maze(n, m)
    maze.start_position = maze.cells[randint(0, maze.width - 1)][maze.height - 1]
    _depth_first_search(maze, maze.start_position)
    maze.reset_visited()
    return maze


def _generate_full_maze(width: int, height: int):
    maze = list()
    for i in range(0, height):
        row = list()
        for j in range(0, width):
            row.append(Cell(x=i, y=j))
        maze.append(row)
    return Maze(maze, (0, 0), width, height)


def _depth_first_search(maze: Maze, cell: Cell):
    stack = []
    cell.visited = True
    stack.append(cell)
    while len(stack) > 0:
        current = stack.pop()
        neigh = maze.get_non_visited_neighbours(current)
        if len(neigh) > 0:
            stack.append(current)
            direction = random.choice(list(neigh.keys()))
            chosen_neigh = neigh[direction]
            connect(current, chosen_neigh, direction)
            chosen_neigh.visited = True
            stack.append(chosen_neigh)
