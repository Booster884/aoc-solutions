with open('input') as f:
    grid = [line.replace('\n', '.') for line in f.readlines()]

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, -1), (1, 1), (-1, 1)]
ans1 = 0
ans2 = 0

def find_adj_nums(x, y):
    nums = set()
    for dir_ in dirs:
        dx, dy = dir_
        try:
            if grid[y + dy][x + dx].isdigit():
                start = end = x + dx
                while grid[y + dy][start].isdigit():
                    start -= 1
                while grid[y + dy][end].isdigit():
                    end += 1
                nums.add(int(grid[y + dy][start+1:end]))
        except IndexError:
            pass
    return nums

for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char not in '.1234567890':
            adj = list(find_adj_nums(x, y))
            ans1 += sum(adj)
            if char == '*' and len(adj) == 2:
                ans2 += adj[0] * adj[1]

print('1:', ans1)
print('2:', ans2)
