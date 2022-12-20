file = open("in", "r")

lines = file.read().split('\n')[:-1]

l = []

for line in lines:
    l.append(int(line) * 811589153)

idx = list(range(len(l)))

for _ in range(10):
    for i in range(len(l)):
        j = idx.index(i)
        idx.pop(j)
        idx.insert((j + l[i]) % len(idx), i)

zero = idx.index(l.index(0))
l = [l[i] for i in idx]

s = 0
for x in [1000, 2000, 3000]:
    s += l[(zero + x) % len(l)]

print(s)
