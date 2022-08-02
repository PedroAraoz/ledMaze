from Generation import generate_depth_first_search_maze
from Solver import breadth_first_search
import utime

MATRIX_SIZE = (8, 8)
SAMPLE_SIZE = 500
MAZE_MIN_LEN = 40


def generate_solved_maze():
    (n, m) = MATRIX_SIZE
    maze = generate_depth_first_search_maze(n, m)
    breadth_first_search(maze)
    return maze


def get_maze(min_steps=MAZE_MIN_LEN):
    while True:
        maze = generate_solved_maze()
        if maze.totalSteps > min_steps:
            return maze


def get_unflattened_steps(maze):
    return list(map(lambda x: list(map(lambda y: y.step, x)), maze.cells))


def get_steps(maze):
    return [val for sublist in get_unflattened_steps(maze) for val in sublist]


def get_maze_and_steps():
    maze = get_maze()
    return maze, get_steps(maze)


delays = []
for i in range(SAMPLE_SIZE):
    to = utime.ticks_ms()
    (maze, steps) = get_maze_and_steps()
    delay = utime.ticks_diff(utime.ticks_ms(), to)
    delays.append(delay)
    print(f"{i + 1}/{SAMPLE_SIZE}")

print(f"sample size: {SAMPLE_SIZE}")
print(f"max delay: {max(delays)}ms")
print(f"min delay: {min(delays)}ms")
print(f"average delay: {sum(delays) / SAMPLE_SIZE}ms")
too_long = [i for i in delays if i > 10*1000]
print(f"{len(too_long)}/{SAMPLE_SIZE} take longer than 10 seconds")
