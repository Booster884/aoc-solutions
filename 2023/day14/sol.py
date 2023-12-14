with open('in') as f:
    rows = f.read().split('\n')

w = len(rows[0])
h = len(rows)

round_rocks = set()
square_rocks = set()

for i, row in enumerate(rows):
    for j, cell in enumerate(row):
        if cell == 'O':
            round_rocks.add((j, i))
        elif cell == '#':
            square_rocks.add((j, i))

for _ in range(100000):
    any_moved = False
    rocks_temp = list(round_rocks)
    for x, y in rocks_temp:
        if (x, y - 1) not in square_rocks.union(round_rocks) and y > 0:
            any_moved = True
            round_rocks.remove((x, y))
            round_rocks.add((x, y - 1))
    if not any_moved:
        break

ans1 = 0
for _, y in round_rocks:
    ans1 += h - y - 1
print(ans1)
