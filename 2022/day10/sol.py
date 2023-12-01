file = open("in", "r")

crt = [['.'] * 40] * 6

l = []
l2 = []
x = 1

for line in file.read().split('\n')[:-1]:
    line = line.split(' ')
    if line[0] == "addx":
        l.append(x)
        x += int(line[1])
        l.append(x)
    elif line[0] == "noop":
        l.append(x)

s1 = 0

for i in range(20, len(l), 40):
    s1 += i * l[i - 2]


print("1:", s1)

l = [1] + l
for y in range(0, 6):
    for x in range(0, 40):
        val = l[y * 40 + x]
        if abs(x - (val + 0)) < 2:
            print('█', end='')
        else:
            print(' ', end='')
    print('')
