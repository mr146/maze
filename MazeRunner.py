from collections import deque
from Point import Point
from State import State


def find_path(maze, bombs_count):
    n = maze.n
    m = maze.m
    shift = [Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0)]
    start_state = State(maze.start, 0)
    was = set({start_state})
    prev = dict()
    queue = deque([start_state])
    win_state = None
    while len(queue) != 0:
        current_state = queue.popleft()
        if current_state.point == maze.finish:
            win_state = current_state
            break
        for direction in range(4):
            new_point = current_state.point + shift[direction]
            new_bombs = current_state.bombs
            if not maze.can_move(current_state.point, new_point):
                new_bombs += 1
            new_state = State(new_point, new_bombs)
            if new_state.valid(n, m, bombs_count) and new_state not in was:
                prev[new_state] = current_state
                was.add(new_state)
                queue.append(new_state)

    if win_state is None:
        return []

    path = [win_state]
    current_state = win_state
    while current_state in prev:
        current_state = prev[current_state]
        path.append(current_state)

    return path