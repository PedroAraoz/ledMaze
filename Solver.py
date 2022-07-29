from Maze import Maze


def pop(lst: list):
    e = lst[0]
    lst.remove(e)
    return e


def breadth_first_search(maze: Maze):
    start = maze.start_position
    start.visited = True
    queue = list()
    queue.append([1, start])
    while len(queue) > 0:
        [step, v] = pop(queue)
        v.visited = True
        v.step = step
        # win condition
        if v.x == maze.height-1:
            maze.totalSteps = step
            return queue
        neighbors = maze.get_valid_non_visited_neighbours(v)
        neighbors = list(map(lambda x: x[1], neighbors.items()))
        for n in neighbors:
            queue.append([step + 1, n])
