from itertools import combinations


with open('in') as f:
    rows = f.read().splitlines()

GROWTH_FACTOR = 1000000 - 1

points = set()

for y, row in enumerate(rows):
    for x, cell in enumerate(row):
        if cell == '#':
            points.add((x, y))

for i in range(len(rows[0]) -1, -1, -1):
    in_column = [(x, y) for x, y in points if x == i]
    if len(in_column) > 0:
        continue
    to_move = []
    for x, y in points:
        if x > i:
            to_move.append((x, y))
    for x, y in to_move:
        points.remove((x, y))
        points.add((x + GROWTH_FACTOR, y))

for i in range(len(rows[0]) -1, -1, -1):
    in_row = [(x, y) for x, y in points if y == i]
    if len(in_row) > 0:
        continue
    to_move = []
    for x, y in points:
        if y > i:
            to_move.append((x, y))
    for x, y in to_move:
        points.remove((x, y))
        points.add((x,  y + GROWTH_FACTOR))

total_distance = 0

for a, b in combinations(points, 2):
    x0, y0 = a
    x1, y1 = b
    distance = abs(x0 - x1) + abs(y0 - y1)
    total_distance += distance

print('1:', total_distance)
