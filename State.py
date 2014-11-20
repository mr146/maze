import copy


class State:
    def __init__(self, point, bombs):
        self.point = point
        self.bombs = bombs
        copy.deepcopy([])

    def valid(self, n, m, bombs_count):
        return in_range(self.point.x, 0, n - 1) and in_range(self.point.y, 0, m - 1) and in_range(self.bombs, 0, bombs_count)

    def __eq__(self, other):
        return self.point == other.point and self.bombs == other.bombs

    def __hash__(self):
        return ((hash(self.point)) * 397) ^ self.bombs

    def __repr__(self):
        return 'x: {0}, y: {1}, bombs: {2}'.format(self.point.x, self.point.y, self.bombs)


def in_range(x, l, r):
    return l <= x <= r