import math


with open('in') as f:
    grid = [line.strip() for line in f.readlines()]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

mapping = {
    '|': {(0, 1): (0, 1), (0, -1): (0, -1)},
    '-': {(1, 0): (1, 0), (-1, 0): (-1, 0)},
    'L': {(0, 1): (1, 0), (-1, 0): (0, -1)},
    'J': {(0, 1): (-1, 0), (1, 0): (0, -1)},
    '7': {(0, -1): (-1, 0), (1, 0): (0, 1)},
    'F': {(0, -1): (1, 0), (-1, 0): (0, 1)},
    '.': {},
}

sx, sy = 0, 0

for i, row in enumerate(grid):
    try:
        sx = row.index('S')
        sy = i
    except ValueError:
        pass

sdir = (None, None)

for dx, dy in dirs:
    n = grid[sy + dy][sx + dx]
    if (dx, dy) in mapping[n]:
        sdir = (dx, dy)
        break

loop_points = {(sx, sy)}

dx, dy = sdir
x, y = sx + dx, sy + dy
i = 0
while (x, y) != (sx, sy) or i == 0:
    n = grid[y][x]
    dx, dy = mapping[n][(dx, dy)]
    loop_points.add((x, y))
    x, y = x + dx, y + dy
    i += 1

print('1:', math.ceil(i/2))

enclosed = set()
w = len(grid[0])
h = len(grid)

for i in range(h):
    in_shape = False
    for j in range(w):
        if (j, i) in loop_points:
            n = grid[i][j]
            # Doesn't work in general, as the starting point could be a 7 or F.
            if n in '7F|':
                in_shape = not in_shape

        if in_shape and (j, i) not in loop_points:
            enclosed.add((j, i))

print('2:', len(enclosed))
