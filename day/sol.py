file = open("in", "r")

l = []
for line in file:
    l.append(int(line))

k = map(lambda x, y: x < y, l[0:-1], l[1:])
m = map(lambda x, y, z: x + y + z, l[0:-2], l[1:-1], l[2:])
m = list(m)
n = map(lambda x, y: x < y, m[0:-1], m[1:])
print(sum(list(k)))
print(sum(list(n)))
