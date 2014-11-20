import copy
from Point import Point


class Maze:
    def __init__(self, n, m, lines):
        self.n = n
        self.m = m
        self.content = lines
        for x in range(0, n):
            for y in range(0, m):
                if lines[2 * x + 1][2 * y + 1] == 'S':
                    self.start = Point(x, y)
                if lines[2 * x + 1][2 * y + 1] == 'E':
                    self.finish = Point(x, y)

    def can_move(self, p_from, p_to):
        return self.content[p_from.x + p_to.x + 1][p_from.y + p_to.y + 1] == '.'

    def render_path(self, path):
        result = copy.deepcopy(self.content)
        for i in range(len(path)):
            cur = path[i]
            set_char(result, cur.point.x * 2 + 1, cur.point.y * 2 + 1, '*')
            if i < len(path) - 1:
                nxt = path[i + 1]
                new_char = '*'
                if not self.can_move(cur.point, nxt.point):
                    new_char = 'X'
                set_char(result, cur.point.x + nxt.point.x + 1, cur.point.y + nxt.point.y + 1, new_char)

        for line in result:
            print(line)


def set_char(lines, x, y, char):
    lines[x] = lines[x][:y] + char + lines[x][y + 1:]