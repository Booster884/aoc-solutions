file = open("in", "r")

l = []
s1 = 0
s2 = 0
for line in file:
    line = line.strip('\n').split(',')
    _ = [[int(x) for x in l.split('-')] for l in line]

    r0 = set(range(_[0][0], _[0][1] + 1))
    r1 = set(range(_[1][0], _[1][1] + 1))
 
    r = r0 & r1
    if r0 == r or r1 == r:
        s1 += 1
    if len(r) > 0:
        s2 += 1

print("1:", s1)
print("2:", s2)
