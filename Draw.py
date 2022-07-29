from Maze import Maze

RESET = '\033[0m'
IMPORTANT_COLOR = '\033[94m'
PATH_COLOR = '\033[95m'


def draw(maze: Maze):
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


def draw_step(steps, s):
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
