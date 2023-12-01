file = open("in", "r")

dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

lines = file.read().split('\n')[:-1]

s1 = 0
s2 = 0
cubes = set()

min_pos = -5
max_pos = 25

for line in lines:
    x, y, z = [int(n) for n in line.split(',')]
    cubes.add((x, y, z))

def in_bounds(pos):
    for n in pos:
        if not (min_pos <= n < max_pos):
            return False
    return True

for cube in cubes:
    for d in dirs:
        dpos = (cube[0] + d[0], cube[1] + d[1], cube[2] + d[2])
        if dpos not in cubes:
            s1 += 1

stack = [(0, 0, 0)]
visited = set()

while len(stack) > 0:
    pos = stack.pop()
    for d in dirs:
        dpos = (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])
 
        can_move = not (dpos in visited or dpos in cubes)
        for n in dpos:
            if not (min_pos <= n < max_pos):
                can_move = False
        if can_move:
            stack.append(dpos)
            visited.add(dpos)
    visited.add(pos)

for pos in visited:
    for d in dirs:
        dpos = (pos[0] + d[0], pos[1] + d[1], pos[2] + d[2])
        if dpos in cubes:
            s2 += 1

print("1:", s1)
print("2:", s2)
