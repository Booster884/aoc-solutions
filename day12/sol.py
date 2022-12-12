heights = 'SabcdefghijklmnopqrstuvwxyzE'

file = open("in", "r")

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = [[*l] for l in file.read().split('\n')[:-1]]

w = len(grid[0])
h = len(grid)

spos = (0, 0)
epos = (0, 0)
for i, row in enumerate(grid):
    if 'S' in row:
        spos = (row.index('S'), i)
    if 'E' in row:
        epos = (row.index('E'), i)

def dist_to_end(spos, epos):
    dirgrid = [[' ' for _ in row] for row in grid]
    curr_height = grid[spos[1]][spos[0]]
    visited = set()
    frontier = [spos]

    while curr_height != 'E' and len(frontier) != 0:
        pos = frontier.pop(0)
        if not(0 <= pos[0] < w) or not(0 <= pos[1] < h):
            continue
        curr_height = grid[pos[1]][pos[0]]

        for d in dirs:
            dpos = (pos[0] + d[0], pos[1] + d[1])
            if not(0 <= dpos[0] < w) or not(0 <= dpos[1] < h):
                continue

            if dpos in visited:
                continue

            dhgt = grid[dpos[1]][dpos[0]]
            if not dhgt in heights:
                continue
            if not curr_height in heights:
                continue

            if heights.index(dhgt) - heights.index(curr_height) <= 1:
                dirgrid[dpos[1]][dpos[0]] = str(dirs.index(d))
                frontier.append(dpos)
                visited.add(dpos)

    # Trace back
    pos = epos

    s = 0
    while pos != spos:
        t = dirgrid[pos[1]][pos[0]]
        if t == ' ':
            return 8320498242039820538957
        d = dirs[int(t)]
        pos = (pos[0] - d[0], pos[1] - d[1])

        s += 1
    return s

# Simply traversing from E to the nearest a would have been quicker, 
# but jank is good!
dists = []
for row in range(h):
    for col in range(w):
        tile = grid[row][col]
        if tile == 'a':
            _spos = (col, row)
            dists.append(dist_to_end(_spos, epos))

print("1:", dist_to_end(spos, epos))
print("2:", min(dists))
