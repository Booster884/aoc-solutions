from itertools import product
from queue import PriorityQueue

neighborhood = [(0, 1), (0, -1), (1, 0), (-1, 0)]

filename = "input"
lines = open(filename).read().splitlines()
points = [line.split(",") for line in lines]
points = [(int(pair[0]), int(pair[1])) for pair in points]

if filename == "test":
    ex, ey = 6, 6
    points_part = points[:12]
else:
    ex, ey = 70, 70
    points_part = points[:1024]

movable = set(product(range(ex + 1), range(ey + 1))) - set(points_part)

def show_grid(seen):
    seen = seen or set()
    for y in range(ey + 1):
        for x in range(ex + 1):
            if (x, y) not in movable:
                print("#", end="")
            elif (x, y) in seen:
                print("o", end="")
            else:
                print(".", end="")
        print()
    print()


def astar(movable, start, end):
    ex, ey = end
    todo = PriorityQueue()
    todo.put((0, start, 0))
    seen = { start: [] }

    while not todo.empty():
        _, curr, path_len = todo.get()
        x, y = curr
        path = seen[curr]
        yield seen

        if curr == end:
            return path_len

        for dir in neighborhood:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if (nx, ny) in movable and (nx, ny) not in seen:
                new_len = path_len + 1
                dist_to_goal = abs(nx - ex) + abs(ny - ey)
                todo.put((new_len + dist_to_goal, (nx, ny), path_len + 1))
                seen[(nx, ny)] = path + [(nx, ny)]


def de_astar(movable, start, end):
    to = astar(movable, start, end)
    fro = astar(movable, end, start)

    while True:
        try:
            a = next(to)
            b = next(fro)
        except StopIteration:
            return set()
        intersection = set(a) & set(b)
        if len(intersection) != 0:
            p = intersection.pop()
            return set(a[p]) | set(b[p])


print(len(de_astar(movable, (0, 0), (ex, ey))) + 1)

movable = set(product(range(ex + 1), range(ey + 1)))
path = set()

for point in points:
    movable.remove(point)
    if len(path) > 0 and point not in path:
        continue
    path = de_astar(movable, (0, 0), (ex, ey))
    if len(path) == 0:
        print(point)
        break
