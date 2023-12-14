with open('in') as f:
    rows = f.read().split('\n')

def grid_string(round_rocks):
    string = ''
    for y in range(h):
        for x in range(w):
            if (x, y) in round_rocks:
                string += 'O'
            elif (x, y) in square_rocks:
                string += '#'
            else:
                string += '.'
        # Not strictly ncessary
    return string

dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

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

seen = {}

i = 0
END = 1000000000 * 4
while i < END:
    if grid_string(round_rocks) in seen and i < 10000:
        cycle_length = i - seen[grid_string(round_rocks)]
        i_left = (END - i) % cycle_length
        i = END - i_left
    rocks_prev = round_rocks.copy()
    round_rocks = set()
    dx, dy = dirs[i % 4]
    for sx, sy in rocks_prev:
        # New position will be that of the first immovable object (wall/rock)
        # minus the number of movable object (round rocks)
        x, y = sx, sy
        num_round = 0
        while x in range(w) and y in range(h - 1) and (x, y) not in square_rocks:
            x, y = x + dx, y + dy
            if (x, y) in rocks_prev:
                num_round += 1

        nx, ny = x - dx * (num_round + 1), y - dy * (num_round + 1)
        round_rocks.add((nx, ny))
    seen[grid_string(rocks_prev)] = i
    i += 1

ans = 0
for _, y in round_rocks:
    ans += h - y - 1
print(ans)
