file = open("in", "r")

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

lines = file.read().split('\n')[:-1]

for line in lines:
    print(line)

print("1:", 1)
print("2:", 2)
