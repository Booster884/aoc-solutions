from itertools import pairwise

with open('in') as f:
    sequences = [list(map(int, line.split())) for line in f.readlines()]

ans1 = 0
ans2 = 0

for seq in sequences:
    ll = [seq]
    while not all([x == 0 for x in ll[-1]]):
        ll.append(list(map(lambda t: t[1] - t[0], pairwise(ll[-1]))))

    for prev, curr in pairwise(ll[::-1]):
        curr[:0] = [curr[0] - prev[0]]
        curr += [curr[-1] + prev[-1]]

    ans1 += ll[0][-1]
    ans2 += ll[0][0]

print('1:', ans1)
print('2:', ans2)
