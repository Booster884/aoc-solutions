heights = 'SabcdefghijklmnopqrstuvwxyzE'

file = open("in", "r")

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = [[*l] for l in file.read().split('\n')[:-1]]
dirgrid = [[' ' for _ in row] for row in grid]
# print(grid)

w = len(grid[0])
h = len(grid)

spos = (0, 0)
epos = (0, 0)
for i, row in enumerate(grid):
    if 'S' in row:
        spos = (row.index('S'), i)
    if 'E' in row:
        epos = (row.index('E'), i)
curr_height = 'S'

visited = set()
frontier = [spos]

i = 0
while curr_height != 'E' and len(frontier) != 0:
    pos = frontier.pop(0)
    # visited.add(pos)
    # print(pos)
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
            # pos = dpos
            # curr_height = dhgt
            frontier.append(dpos)
            visited.add(dpos)
            # break

    # i += 1
    # if i > 10:
    #     break

# Trace back
pos = epos

for row in dirgrid:
    print(''.join(row))

s = 0
while pos != spos:
    print(pos)
    t = dirgrid[pos[1]][pos[0]]
    d = dirs[int(t)]
    pos = (pos[0] - d[0], pos[1] - d[1])

    s += 1

    i += 1
    if i > 1000:
        break

print("1:", s)
print("2:")
