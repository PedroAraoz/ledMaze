import matplotlib.pyplot as plt

from Carve import randomCarve
from Draw import draw
from Generation import generateFullMaze
from Solver import BFS

n, m = (8, 8)
base = generateFullMaze(n, m)
while True:
    maze = randomCarve(base)
    BFS(maze)
    print("asd")
    draw(maze, plt)
    plt.show()
