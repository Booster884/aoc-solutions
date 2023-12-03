with open('input') as f:
    grid = [line.replace('\n', '.') for line in f.readlines()]

numbers = []

curr = ''
for y, line in enumerate(grid):
    for x, char in enumerate(line):
        if char.isdigit():
            curr += char
        elif curr != '':
            pos = (x - len(curr), y)
            numbers.append((pos, curr))
            curr = ''

ans1 = 0

for num in numbers:
    pos, curr = num
    x, y = pos

    is_symbol_adj = []
    for i in range(y - 1, y + 2):
        for j in range(x - 1, x + len(curr) + 1):
            try:
                is_symbol_adj.append(grid[i][j] not in '1234567890.')
            except IndexError:
                pass
    if any(is_symbol_adj):
        ans1 += int(curr)

print('1:', ans1)
