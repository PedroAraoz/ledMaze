from Cell import Cell
from Maze import Maze

RESET = '\033[0m'
IMPORTANT_COLOR = '\033[94m'
PATH_COLOR = '\033[95m'


def print_maze(maze: Maze):
    steps = list(map(lambda x: list(map(lambda y: y.step, x)), maze.cells))
    for row in steps:
        print("[", end='')
        for step in row:
            if step == maze.start_position.step or step == maze.totalSteps:
                print(IMPORTANT_COLOR, end='')
            elif step != 0:
                print(PATH_COLOR, end='')
            print("%3s" % step, end=f'{RESET},')
        print("]")


def print_solved(maze):
    for cells in maze.cells:
        print("[", end='')
        for c in cells:
            if (c.y + 8 * c.x) in maze.path:
                print(IMPORTANT_COLOR, end='')
            elif c != 0:
                print(PATH_COLOR, end='')
            print("%3s" % c.step, end=f'{RESET},')
        print("]")


def print_step(steps, s):
    print('\n\n\n\n\n')
    for row in steps:
        print("[", end='')
        for step in row:
            if step == s:
                print(IMPORTANT_COLOR, end='')
            elif step != 0:
                print(PATH_COLOR, end='')
            print("%3s" % step, end=f'{RESET},')
        print("]")
