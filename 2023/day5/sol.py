with open('input') as f:
    maps = f.read().split('\n\n')

seeds = [int(x) for x in maps[0].split(': ')[1].split()]
seeds = list(zip(seeds[0::2], seeds[1::2]))

mappings = []
for map_str in maps[1:]:
    ranges = map_str.splitlines()[1:]
    mappings.append([[int(x) for x in r.split()] for r in ranges])

for i in range(10000000000000):
    x = i
    for mapping in mappings[::-1]:
        for dest, src, length in mapping:
            if x >= dest and x < dest + length:
                x += src - dest
                break

    for start, length in seeds:
        if x >= start and x < start + length:
            print(i)
            exit()
