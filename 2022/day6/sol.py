file = open("in", "r")

for line in file.read().split('\n')[:-1]:
    for i in range(0, len(line)):
        a = line[i:i+4]
        if (len(set(a)) == 4):
            print("1:", i+4)
            break

    for i in range(0, len(line)):
        a = line[i:i+14]
        if (len(set(a)) == 14):
            print("2:", i+14)
            break
