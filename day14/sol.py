file = open("in", "r")

dirs = [(0, 1), (-1, 1), (1, 1)]

def sign(a):
    if a < 0:
        return -1
    elif a > 0:
        return 1
    return 0

w = 1000
h = 200
grid = []
for _ in range(h):
    grid.append([' '] * w)

maxy = 0
s = 0

# Create walls
for line in file.read().split('\n')[:-1]:
    line = line.split(" -> ")
    line = [coord.split(',') for coord in line]
    line = [(int(c[0]), int(c[1])) for c in line]

    pos = line[0]
    grid[pos[1]][pos[0]] = '#'
    for i in range(len(line) - 1):
        d = (sign(line[i+1][0] - line[i][0]), sign(line[i+1][1] - line[i][1]))
        while pos != line[i+1]:
            pos = (pos[0] + d[0], pos[1] + d[1])
            grid[pos[1]][pos[0]] = '#'
        maxy = max(maxy, pos[1])

maxy += 2
print(maxy)

# Simulate sand
def hah():
    s = 0
    for _ in range(1000000):
        pos = (500, 0)
        if grid[0][500] == 'o':
            return s
        resting = False
        while not resting:
            resting = True
            for d in dirs:
                dpos = (pos[0] + d[0], pos[1] + d[1])
                if not (0 < dpos[0] < w and 0 < dpos[1] < h):
                    return s
                if grid[dpos[1]][dpos[0]] == ' ' and dpos[1] < maxy:
                    pos = dpos
                    resting = False
                    break
            if resting:
                grid[pos[1]][pos[0]] = 'o'
                s += 1
                break

print("2:", hah())
