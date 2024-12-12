from itertools import product

neighborhood = [(0,1), (1, 0), (0, -1), (-1, 0)]

grid = open("input").read().splitlines()
w, h = len(grid[0]), len(grid)

grid_set = set(product(range(w), range(h)))

def flood(grid, x, y):
    c = grid[y][x]
    stack = [(x, y)]
    region = set([(x, y)])

    while len(stack) > 0:
        x, y = stack.pop()
        for nx, ny in [(x + dx, y + dy) for dx, dy in neighborhood]:
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in region and grid[ny][nx] == c:
                stack.append((nx, ny))
                region.add((nx, ny))

    return region

def area(region):
    return len(region)

def perimeter(region):
    p = 0
    for (x, y) in region:
        for nx, ny in [(x + dx, y + dy) for dx, dy in neighborhood]:
            if (nx, ny) not in region:
                p += 1
    return p

regions = []
while len(grid_set) > 0:
    (x, y) = grid_set.pop()
    region = flood(grid, x, y)
    regions.append(region)
    grid_set -= region

part1 = 0
for region in regions:
    part1 += area(region) * perimeter(region)

print(part1)
