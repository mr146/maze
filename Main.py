import sys
from InputFileParser import parse
from MazeRunner import find_path

args = sys.argv[1:]
input_file_name = args[0]
[height, width, bombs_count, maze] = parse(input_file_name)

result = find_path(maze, bombs_count)
if not result:
    print("No exit")
else:
    maze.render_path(result)