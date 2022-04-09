import matplotlib.pyplot as plt

from Draw import draw
from Generation import depthFirstSearchMaze

n, m = (8, 8)
while True:
    maze = depthFirstSearchMaze(n, m)
    draw(maze, plt)
    plt.show()
