from collections import defaultdict
from functools import reduce
from operator import mul


with open('input') as f:
    lines = f.readlines()

allowed = {'red': 12, 'green': 13, 'blue': 14}
ans1 = 0
ans2 = 0

for line in lines:
    game_id, game = line.strip().split(': ')
    game_id = int(game_id.split()[-1])

    shows = game.split('; ')
    fits = []
    seen = defaultdict(list)

    for show in shows:
        pairs = [pair.split(' ') for pair in show.split(', ')]
        fits.append(all([int(pair[0]) <= allowed[pair[1]] for pair in pairs]))
        for pair in pairs:
            seen[pair[1]].append(int(pair[0]))

    if all(fits):
        ans1 += game_id
    ans2 += reduce(mul, [max(x) for x in seen.values()], 1)

print('1:', ans1)
print('2:', ans2)
