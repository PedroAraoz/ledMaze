from Generation import generate_depth_first_search_maze
from Solver import breadth_first_search
import utime

MATRIX_SIZE = (8, 8)
SAMPLE_SIZE = 1000


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


delays = []
for i in range(SAMPLE_SIZE):
    to = utime.ticks_ms()
    maze = get_maze(30)
    steps = get_steps(maze)
    delay = utime.ticks_diff(utime.ticks_ms(), to)
    delays.append(delay)
    print(f"{i+1}/{SAMPLE_SIZE}")

print(f"sample size: {SAMPLE_SIZE}")
print(f"max delay: {max(delays)}ms")
print(f"min delay: {min(delays)}ms")
print(f"average delay: {sum(delays) / SAMPLE_SIZE}ms")
