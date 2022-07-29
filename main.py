from Generation import generate_depth_first_search_maze
from Solver import breadth_first_search

MATRIX_SIZE = (8, 8)


def _generate_solved_maze():
    (n, m) = MATRIX_SIZE
    maze = generate_depth_first_search_maze(n, m)
    breadth_first_search(maze)
    return maze


def get_maze(min_steps):
    while True:
        maze = _generate_solved_maze()
        if maze.totalSteps > min_steps:
            return maze


def get_steps(maze):
    return list(map(lambda x: list(map(lambda y: y.step, x)), maze.cells))


maze = get_maze(30)
steps = get_steps(maze)
for step in steps:
    print(step)
