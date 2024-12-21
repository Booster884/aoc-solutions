from collections import deque
from functools import cache, reduce
from itertools import pairwise, product
from math import inf

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


def find_paths(start, end, movable):
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
        paths = find_paths(curr, goal, movable)
        parts_ = []
        for path in paths:
            parts_ += [part + path for part in parts]
        parts = parts_
        curr = goal

    return parts


@cache
def lowest_path_cost(sequence: str, level: int) -> int:
    if level == 0:
        return len(sequence)
    path = 0
    for a, b in pairwise("A" + sequence):
        options = best_dir_moves[(a, b)]
        paths = [lowest_path_cost(opt, level - 1) for opt in options]
        path += sorted(paths)[0]
    return path


best_dir_moves = {}

for start, end in product(dir_positions, repeat=2):
    p = find_paths(dir_positions[start], dir_positions[end], dir_positions.values())
    best_dir_moves[(start, end)] = p

lines = open("input").read().splitlines()

def solve(iterations):
    sol = 0

    for line in lines:
        best = inf
        p = paths(line, num_positions)
        for p_ in p:
            best = min(lowest_path_cost(p_, iterations), best)
        sol += int(line[:-1]) * best

    return sol

print(solve(2))
print(solve(25))
