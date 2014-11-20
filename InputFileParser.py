from Maze import Maze


def parse(filename):
    input_file = open(filename, 'r')
    [height, width, bombs_count] = [int(x) for x in input_file.readline().split(' ')[:3]]
    lines = [input_file.readline().strip() for x in range(0, 2 * height + 1)]
    maze = Maze(height, width, lines)
    return [height, width, bombs_count, maze]
