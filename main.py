from Printer import printMaze
from Generation import generate_depth_first_search_maze
from Solver import breadth_first_search
from neopixel import Neopixel
import time
import _thread

MATRIX_SIZE = (8, 8)
MAZE_MIN_LEN = 39
LEDS = 8 * 8
strip = Neopixel(LEDS, 0, 0, "GRB")
strip.brightness(8)
# Color variables
MAIN_COLOR = (60, 56, 255)
PATH_COLOR = (0, 255, 0)
# Thread variables
global newMaze
newMaze = (None, None)
global usedMaze
usedMaze = True


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


def maze_generation_thread():
    global newMaze
    global usedMaze
    while True:
        if usedMaze:
            newMaze = get_maze_and_steps()
            usedMaze = False
            # print('new maze generated')
        time.sleep(0.3)


def clear():
    strip.clear()
    strip.show()


def draw_path():
    for i in path:
        strip.set_pixel(i, PATH_COLOR)
        strip.show()
        time.sleep(0.08)


def flash_path(times=2, delay=0.3):
    for _ in range(times):
        for i in path: strip.set_pixel(i, MAIN_COLOR)
        strip.show()
        time.sleep(delay)
        for i in path:  strip.set_pixel(i, PATH_COLOR)
        strip.show()
        time.sleep(delay)


_thread.start_new_thread(maze_generation_thread, ())
time.sleep(1)
while True:
    global usedMaze
    if not usedMaze:
        global newMaze
        current_step = 1
        (maze, steps) = newMaze
        printMaze(maze)
        path = maze.path
        usedMaze = True
        clear()
        while current_step <= maze.totalSteps:
            for index, val in enumerate(steps):
                if val == current_step:
                    strip.set_pixel(index, PATH_COLOR)
            strip.show()
            current_step += 1
            time.sleep(0.11)
        time.sleep(0.5)
        draw_path()
        time.sleep(0.1)
        flash_path()
        time.sleep(1)
