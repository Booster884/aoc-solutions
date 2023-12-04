from collections import defaultdict


with open('input') as f:
    lines = f.readlines()

ans1 = 0
amounts = defaultdict(int)

for i, line in enumerate(lines):
    winning, have = line.split(' | ')
    _, winning = winning.split(': ')
    winning = {int(x) for x in winning.split()}
    have = {int(x) for x in have.split()}
    winning_count = len(have & winning)

    amounts[i] += 1
    if winning_count > 0:
        ans1 += 2 ** (winning_count - 1)
        for j in range(i + 1, i + winning_count + 1):
            amounts[j] += amounts[i]

print('1:', ans1)
print('2:', sum(v for v in amounts.values()))
