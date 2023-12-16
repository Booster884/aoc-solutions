with open('in') as f:
    GRID = f.read().split('\n')

w = range(len(GRID[0]))
h = range(len(GRID) - 1)

def energised(x, y, dx, dy):
    SEEN = set()
    SEENDIR = set()

    frontier = [(x, y, dx, dy)]

    while len(frontier) > 0:
        x, y, dx, dy = frontier.pop()
        if (x not in w) or (y not in h):
            continue
        if (x, y, dx, dy) in SEENDIR:
            continue

        SEEN.add((x, y))
        SEENDIR.add((x, y, dx, dy))
        match GRID[y][x], dx, dy:
            case ['.', *_]:
                frontier.append((x + dx, y + dy, dx, dy))
            case ['/', *_]:
                dx, dy = -dy, -dx
                frontier.append((x + dx, y + dy, dx, dy))
            case ['\\', *_]:
                dx, dy = dy, dx
                frontier.append((x + dx, y + dy, dx, dy))
            case ['|', 0, _]:
                frontier.append((x + dx, y + dy, dx, dy))
            case ['|', *_]:
                frontier.append((x, y + 1, 0, 1))
                frontier.append((x, y - 1, 0, -1))
            case ['-', _, 0]:
                frontier.append((x + dx, y + dy, dx, dy))
            case ['-', *_]:
                frontier.append((x + 1, y, 1, 0))
                frontier.append((x - 1, y, -1, 0))
            case _:
                frontier.append((x + dx, y + dy, dx, dy))

    return len(SEEN)

starts = []

for x in w:
    starts.append((x, 0, 0, 1))
    starts.append((x, len(GRID) - 1, 0, -1))

for y in h:
    starts.append((0, y, 1, 0))
    starts.append((len(GRID[0]) - 1, y, -1, 0))

print('1:', energised(0, 0, 1, 0))
print('2:', max([energised(*args) for args in starts]))
