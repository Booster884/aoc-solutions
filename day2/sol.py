file = open("in", "r")

s = 0;
for line in file:
    _ = line.replace('\n', '').split(' ')
    a = ord(_[0]) - ord('A')
    b = ord(_[1]) - ord('X')

    n = 0;
    n += b + 1
    if a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 0:
        n += 6
    elif a == b:
        n += 3
    s += n

print("1:", s)

file = open("in", "r")

s = 0;
for line in file:
    _ = line.replace('\n', '').split(' ')
    a = ord(_[0]) - ord('A')
    b = ord(_[1]) - ord('X')

    if b == 0:
        b = (a + 2) % 3
    elif b == 1:
        b = a
    elif b == 2:
        b = (a + 1) % 3

    n = 0;
    n += b + 1
    if a == 0 and b == 1 or a == 1 and b == 2 or a == 2 and b == 0:
        n += 6
    elif a == b:
        n += 3
    s += n

print("2:", s)
