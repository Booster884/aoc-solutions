with open('in') as f:
    grids = f.read().split('\n\n')

def distance(a, b):
    dist = 0
    for i in range(min(len(a), len(b))):
        dist += a[i] != b[i]
    return dist

def mirror_point(grid, smudge):
    for i in range(len(grid[0]) - 1):
        dists = []
        for row in grid:
            left, right = row[i::-1], row[i+1:]
            dists.append(distance(left, right))
        if sum(dists) == int(smudge):
            return i + 1
    return 0

ans1 = 0
ans2 = 0

for grid in grids:
    grid = grid.splitlines()
    ans1 += mirror_point(grid, False)
    ans2 += mirror_point(grid, True)

    grid = list(zip(*grid))
    ans1 += mirror_point(grid, False) * 100
    ans2 += mirror_point(grid, True) * 100

print('1:', ans1)
print('2:', ans2)
