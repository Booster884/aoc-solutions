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


def bfs(walls, start, end):
    todo = [(start, 0)]
    seen = dict()

    while len(todo) > 0:
        curr, path_len = todo.pop()
        x, y = curr

        seen[(x, y)] = path_len

        if curr == end:
            return seen

        for dx, dy in neighborhood:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in walls and (nx, ny) not in seen:
                todo.append(((nx, ny), path_len + 1))

    return dict()


# Here we intend to check all tiles in range anyway, so ordering of `todo`
# doesn't matter here either.
def cheat(path, start, length):
    x, y = start
    poss = []

    for nx in range(x-length, x+length+1):
        for ny in range(y-length, y+length+1):
            dist = abs(x - nx) + abs(y - ny)
            if dist <= length and (nx, ny) in path:
                poss.append((path[(nx, ny)], dist))

    return poss


path = bfs(walls, start, end)

part1 = 0

for point in path:
    time = path[point]
    cheats = cheat(path, point, 2)
    time_saves = [time - v - l for v, l in cheats if time - v - 2 > 0]
    for time_save in time_saves:
        if time_save >= 100:
            part1 += 1

print(part1)

part2 = 0

for point in path:
    time = path[point]
    cheats = cheat(path, point, 20)
    time_saves = [time - val - l for val, l in cheats]
    for time_save in time_saves:
        if time_save >= 100:
            part2 += 1

print(part2)
