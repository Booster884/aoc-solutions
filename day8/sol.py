file = open("in", "r")

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

grid = file.read().split('\n')[:-1]
grid = [[int(tile) for tile in row] for row in grid]

h = len(grid)
w = len(grid[0])

scores = []

s1 = 0
for row in range(1, h - 1):
    for col in range(1, w - 1):
        visible = []
        height = grid[row][col]
        visible = []
        dists = []
        for d in dirs:
            visible.append(1)
            r = row
            c = col
            while 0 < r < w-1 and 0 < c < h-1:
                r += d[0]
                c += d[1]
                if grid[r][c] >= height:
                    visible[-1] = 0
                    break
            dists.append(abs(row - r) + abs(col - c))

        score = dists[0] * dists[1] * dists[2] * dists[3]
        scores.append(score)

        if sum(visible) > 0:
            s1 += 1

        # print(grid[row][col])

s1 += w * h - (w-2) * (h-2)

print("1:", s1)
print("2:", max(scores))
