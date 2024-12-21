from collections import deque
from functools import reduce

dirs = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1),
}

num_positions = {
    "7": (0, 0), "8": (1, 0), "9": (2, 0),
    "4": (0, 1), "5": (1, 1), "6": (2, 1),
    "1": (0, 2), "2": (1, 2), "3": (2, 2),
                 "0": (1, 3), "A": (2, 3),
}

dir_positions = {
                 "^": (1, 0), "A": (2, 0),
    "<": (0, 1), "v": (1, 1), ">": (2, 1),
}


def flatten_list(l):
    return reduce(lambda a, b: a + b, l)


def find_path(start, end, movable):
    todo = deque([(start, "")])
    seen = set()
    paths = []

    while len(todo) > 0:
        curr, path = todo.popleft()
        x, y = curr

        seen.add(curr)

        if curr == end:
            paths.append(path + "A")
            continue

        for c, dir in dirs.items():
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if (nx, ny) not in seen and (nx, ny) in movable:
                todo.append(((nx, ny), path + c))

    return paths


def paths(sequence, positions):
    movable = positions.values()
    curr = positions["A"]
    parts = [""]
    for c in sequence:
        goal = positions[c]
        paths = find_path(curr, goal, movable)
        parts_ = []
        for path in paths:
            parts_ += [part + path for part in parts]
        parts = parts_
        curr = goal

    return parts

lines = open("input").read().splitlines()

part1 = 0

for line in lines:
    p = paths(line, num_positions)
    for _ in range(2):
        best_len = min(len(x) for x in p)
        best_p = [x for x in p if len(x) == best_len]
        p_ = flatten_list([paths(xs, dir_positions) for xs in best_p])
        p = p_
    best_len = min(len(x) for x in p)
    part1 += int(line[:-1]) * best_len
print(part1)
