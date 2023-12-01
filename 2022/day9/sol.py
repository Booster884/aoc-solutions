file = open("in", "r")

dir_names = 'RDLU'
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
diag_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

rope = [(0,0)] * 10

visited = set()

def sign(n):
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0

def move(hpos, tpos):
    for td in dirs + diag_dirs + [(0, 0)]:
        if (tpos[0] + td[0], tpos[1] + td[1]) == hpos:
            return tpos

    d = (tpos[0] - hpos[0], tpos[1] - hpos[1])

    if d == (2, 0):
        tpos = (hpos[0] + 1, hpos[1])
    elif d == (-2, 0):
        tpos = (hpos[0] - 1, hpos[1])
    elif d == (0, 2):
        tpos = (hpos[0], hpos[1] + 1)
    elif d == (0, -2):
        tpos = (hpos[0], hpos[1] - 1)
    else:
        tpos = (tpos[0] - sign(d[0]), tpos[1] - sign(d[1]))
 
    return tpos

for line in file.read().split('\n')[:-1]:
    line = line.split(' ')
    d = dirs[dir_names.index(line[0])]
    n = int(line[1])

    for i in range(n):
        rope[0] = (rope[0][0] + d[0], rope[0][1] + d[1])

        for j in range(0, len(rope) - 1):
            tpos = move(rope[j], rope[j + 1])
            rope[j + 1] = tpos

        visited.add(rope[-1])

print(len(visited))
