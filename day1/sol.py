file = open("in", "r")

s = 0
l = []
for line in file:
    if line == '\n':
        l.append(s)
        s = 0
    else:
        s += int(line)
l.append(s)

l = sorted(l)

print(max(l))
print(l[-1] + l[-2] + l[-3])
