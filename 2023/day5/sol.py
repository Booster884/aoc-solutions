with open('input') as f:
    maps = f.read().split('\n\n')

seeds = [int(x) for x in maps[0].split(': ')[1].split()]

for mapping in maps:
    ranges = mapping.splitlines()[1:]
    mapped = [False] * len(seeds)
    for range_ in ranges:
        dest_start, src_start, length = [int(x) for x in range_.split()]
        dest = range(dest_start, dest_start + length)
        src = range(src_start, src_start + length)

        for i, seed in enumerate(seeds):
            if seed in src and not mapped[i]:
                seeds[i] = dest[src.index(seed)]
                mapped[i] = True

print('1:', min(seeds))
