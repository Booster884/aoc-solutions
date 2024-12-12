from itertools import product

neighborhood = [(0,1), (1, 0), (0, -1), (-1, 0)]

grid = open("input").read().splitlines()
w, h = len(grid[0]), len(grid)

grid_set = set(product(range(w), range(h)))

grid_map = {(x, y): grid[y][x] for (x,y) in product(range(w), range(h))}

def flood(map, x, y):
    c = map[(x, y)]
    stack = [(x, y)]
    region = set([(x, y)])

    while len(stack) > 0:
        x, y = stack.pop()
        for nx, ny in [(x + dx, y + dy) for dx, dy in neighborhood]:
            if (nx, ny) in map and (nx, ny) not in region and map[(nx, ny)] == c:
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

def edges(region):
    e = 0
    for dx, dy in neighborhood:
        hmm = {(x + dx, y + dy): "?" for (x, y) in region if (x + dx, y + dy) not in region}
        e += len(split_regions(hmm))
    return e

def split_regions(map):
    todo = set(map.keys())
    regions = []
    while len(todo) > 0:
        (x, y) = todo.pop()
        region = flood(map, x, y)
        regions.append(region)
        todo -= region
    return regions

regions = split_regions(grid_map)

part1 = part2 = 0
for region in regions:
    part1 += area(region) * perimeter(region)
    part2 += area(region) * edges(region)

print(part1)
print(part2)
