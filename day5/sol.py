file = open("in", "r")

docks = [0, [], [], [], [], [], [], [], [], []]
div = 8

for line in file.read().split('\n')[:div]:
    i = 1
    for crate in line[1::4]:
        if crate != ' ':
            docks[i] = [crate] + docks[i]
        i += 1

file.seek(0)
for line in file.read().split('\n')[div+2:-1]:
    line = line.strip("move ").split(" ")[::2]
    count, start, end = [int(x) for x in line]

    # Part 1
    # for i in range(count):
    #     docks[end].append(docks[start].pop())

    # Part 2
    docks[end] += docks[start][-count:]
    for i in range(count):
        docks[start].pop()

for dock in docks[1:]:
    if len(dock) > 0:
        print(dock[-1])
    else:
        print("")

# Now manually remove newlines and submit :)
