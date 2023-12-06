import math

with open('input') as f:
    times, distances = f.readlines()
    times = [int(t) for t in times.split(':')[1].split()]
    distances = [int(d) for d in distances.split(':')[1].split()]
    races = zip(times, distances)

def win_count(time, distance):
    return sum([t * (time - t) > distance for t in range(time)])

print('1:', math.prod(win_count(*race) for race in races))

time = int(''.join(str(t) for t in times))
distance = int(''.join(str(d) for d in distances))

print('2:', win_count(time, distance))
