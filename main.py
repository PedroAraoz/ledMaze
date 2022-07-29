from Draw import draw
from Generation import generate_depth_first_search_maze
from Solver import breadth_first_search
from neopixel import Neopixel
import time
import _thread

MATRIX_SIZE = (8, 8)
LEDS = 8 * 8
strip = Neopixel(LEDS, 0, 0, "GRB")
strip.brightness(8)
# Color definitions
head = (34, 56, 255)
middle = (255, 35, 0)
tail = (20, 20, 0)
blank = (0, 0, 0)

global newMaze
newMaze = (None, None)
global usedMaze
usedMaze = True


def generate_solved_maze():
    (n, m) = MATRIX_SIZE
    maze = generate_depth_first_search_maze(n, m)
    breadth_first_search(maze)
    return maze


def get_maze(min_steps=39):
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
            #print('new maze generated')
        time.sleep(0.3)


_thread.start_new_thread(maze_generation_thread, ())
time.sleep(1)
while True:
    global usedMaze
    if not usedMaze:
        global newMaze
        current_step = 1
        (maze, steps) = newMaze
        draw(maze)
        usedMaze = True
        strip.clear()
        strip.show()
        while current_step <= maze.totalSteps:
            for index, val in enumerate(steps):
                if val == current_step:
                    strip.set_pixel(index, ((34*val)%255, 56, 255))
                #elif val == current_step - 1:
                    #strip.set_pixel(index, middle)
                #elif val == current_step - 2:
                    #strip.set_pixel(index, head)
                #else:
                    #strip.set_pixel(index, blank)
            strip.show()
            current_step += 1
            time.sleep(0.11)
