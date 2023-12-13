with open('in') as f:
    grids = f.read().split('\n\n')

ans1 = 0

def mirror_point(grid) -> int:
    for i in range(len(grid[0]) - 1):
        same = []
        for row in grid:
            left, right = row[i+1::-1], row[i:]
            size = min(len(left), len(right))
            left, right = left[:size], right[:size]
            same.append(left == right)
        if all(same):
            return i + 1
    return 0

for grid in grids:
    grid = grid.splitlines()
    ans1 += mirror_point(grid)
    grid = list(zip(*grid))
    ans1 += mirror_point(grid) * 100

print('1:', ans1)
