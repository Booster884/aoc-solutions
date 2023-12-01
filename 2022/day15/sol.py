import re
file = open("in", "r")
area = 4000000

def simplify(arr):
    new_arr = []
    s, e = arr[0]
    for i in range(1, len(arr)):
        if arr[i][0] <= e:
            e = max(e, arr[i][1])
        else:
            new_arr.append((s, e))
            s, e = arr[i]

    new_arr.append((s, e))
    return new_arr

data = file.read()
scanners = []
p = re.compile(r"-?\d+")

for line in data.split('\n')[:-1]:
    sx, sy, bx, by = [int(n) for n in p.findall(line)]
    r = abs(sx - bx) + abs(sy - by)
    scanners.append((sx, sy, r))

for y in range(area):
    inters = []
    for s in scanners:
        dy = abs(y - s[1])
        r = s[2] - dy
        if r > 0:
            inters.append((s[0] - r, s[0] + r))
    inters.sort(key=lambda x: x[0])
    inters = simplify(inters)
    if len(inters) == 2 and (inters[1][0] - inters[0][1] == 2):
        x = inters[0][1] + 1
        print(x * 4000000 + y)
        quit()


