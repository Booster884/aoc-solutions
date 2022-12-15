import re
file = open("in", "r")
qy = 2000000
# qy = 10

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

data = file.read()
# grid = [[*l] for l in data.split('\n')[:-1]]

s = 0
l = []

blocked = set()
beacons = set()

p = re.compile(r"-?\d+")
for line in data.split('\n')[:-1]:
    sx, sy, bx, by = [int(n) for n in p.findall(line)]
    r = abs(sx - bx) + abs(sy - by)
    r = r - abs(qy - sy)
    for x in range(sx - r, sx + r + 1):
        blocked.add(x)
    if by == qy:
        beacons.add(bx)

print("1:", len(blocked) - len(beacons))
print("2:")
# 5294935 high
