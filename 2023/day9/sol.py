from itertools import pairwise

with open('in') as f:
    sequences = [list(map(int, line.split())) for line in f.readlines()]

ans1 = []

for seq in sequences:
    ll = [seq]
    while not all(i == 0 for i in ll[-1]) and len(ll[-1]) > 0:
        ll.append(list(map(lambda t: t[1] - t[0], pairwise(ll[-1]))))
    ll = list(reversed(ll))

    for i, l in enumerate(ll):
        if i == 0:
            ll[i].append(0)
        else:
            ll[i].append(l[-1] + ll[i - 1][-1])
    ans1.append(ll[-1][-1])

print('1:', sum(ans1))
