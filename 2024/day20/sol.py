from collections import defaultdict, deque

neighborhood = [(0,1), (1, 0), (0, -1), (-1, 0)]

grid = open("input").read().strip()
grid = grid.splitlines()
walls = set()
start = (0, 0)
end = (0, 0)
w, h = len(grid[0]), len(grid)

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "#":
            walls.add((x, y))
        elif cell == "S":
            start = (x, y)
        elif cell == "E":
            end = (x, y)


# It really doesn't matter how `todo` is ordered, there is always one tile left.
def bfs(walls, start, end):
    todo = deque([(start, 0)])
    seen = dict()

    while len(todo) > 0:
        curr, path_len = todo.popleft()
        x, y = curr

        seen[(x, y)] = path_len

        if curr == end:
            return seen

        for dx, dy in neighborhood:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls and (nx, ny) not in seen:
                todo.append(((nx, ny), path_len + 1))

    return dict()


path = bfs(walls, start, end)
path_len = path[end]

seen = defaultdict(int)
part1 = 0

for x, y in path:
    for dx, dy in neighborhood:
        nx, ny = x + dx, y + dy
        if (nx, ny) in walls and (nx + dx, ny + dy) in path:
            time_saved = path[(x, y)] - path[(nx + dx, ny + dy)] - 2

            if time_saved > 0:
                seen[time_saved] += 1
            if time_saved >= 100:
                part1 += 1

print(part1)
