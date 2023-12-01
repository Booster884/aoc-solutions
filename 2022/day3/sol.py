al = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
file = open("in", "r")

s1 = 0
s2 = 0
i = 0
common = set(al)

for line in file.read().split('\n'):
    half = int(len(line)/2)
    l0 = set(line[:half])
    l1 = set(line[half:])

    s1 += sum([al.find(c) for c in l0 & l1])

    common &= l0 | l1

    if i % 3 == 2:
        s2 += sum([al.find(c) for c in common])
        common = set(al)

    i += 1

print("1:", s1)
print("2:", s2)
