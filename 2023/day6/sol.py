from functools import reduce
from operator import mul

with open('input') as f:
    times, distances = f.readlines()
    times = [int(t) for t in times.split(':')[1].split()]
    distances = [int(d) for d in distances.split(':')[1].split()]
    races = zip(times, distances)

ans1 = []
for time, distance in races:
    c = [t * (time - t) for t in range(time)]
    winning = [d for d in c if d > distance]
    ans1.append(len(winning))

print('1:', reduce(mul, ans1, 1))

time = int(''.join(str(t) for t in times))
distance = int(''.join(str(d) for d in distances))

c = [t * (time - t) for t in range(time)]
winning = [d for d in c if d > distance]
ans2 = len(winning)

print('2:', ans2)
