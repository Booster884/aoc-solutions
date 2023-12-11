from itertools import combinations


with open('in') as f:
    rows = f.read().splitlines()

def expand(rows):
    empty = []
    for i, row in enumerate(rows):
        if all(c == '.' for c in row):
            empty.append(i)
    for i in empty[::-1]:
        rows.insert(i, '.' * len(rows[0]))

expand(rows)
transposed_rows = [list(col) for col in zip(*rows)]
expand(transposed_rows)

points = set()

for x, column in enumerate(transposed_rows):
    for y, cell in enumerate(column):
        if cell == '#':
            points.add((x, y))

total_distance = 0

for a, b in combinations(points, 2):
    x0, y0 = a
    x1, y1 = b
    distance = abs(x0 - x1) + abs(y0 - y1)
    total_distance += distance

print('1:', total_distance)
