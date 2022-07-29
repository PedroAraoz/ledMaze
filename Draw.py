from Maze import Maze

RESET = '\033[0m'
IMPORTANT_COLOR = '\033[94m'
PATH_COLOR = '\033[95m'


def draw(maze: Maze, steps):
    for row in steps:
        print("[", end='')
        for step in row:
            if step == maze.start_position.step or step == maze.totalSteps:
                print(IMPORTANT_COLOR, end='')
            elif step != 0:
                print(PATH_COLOR, end='')
            print("%3s" % step, end=f'{RESET},')
        print("]")
