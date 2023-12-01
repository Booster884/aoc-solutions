import random
import re
file = open("in", "r")

lines = file.read().split('\n')[:-1]

vertices = {}
visited = {}
edges = {}

def bfs(start):
    visited = {}
    dists = {start: 0}
    for key in vertices:
        visited[key] = False

    queue = []
    queue.append(start)

    while len(queue) > 0:
        curr = queue.pop(0)
        visited[curr] = True
        for neighbor in vertices[curr][1]:
            if visited[neighbor] == False:
                dists[neighbor] = dists[curr] + 1
                queue.append(neighbor)

    _dists = {}
    for key in dists:
        if vertices[key][0] != 0 and dists[key] != 0:
            _dists[key] = dists[key]
    return _dists

def rec_desc(curr, paths_left, time_left):
    if time_left <= 0:
        return 0

    if paths_left == None or len(paths_left) == 0:
        press = vertices[curr][0]
        return press * time_left

    a = []
    for n in paths_left:
        next_paths = paths_left.copy()
        next_paths.remove(n)
        next_time = time_left - 1 - edges[curr][n]
        a.append(rec_desc(n, next_paths, next_time))

    press = vertices[curr][0]
    return press * time_left + max(a)


for line in lines:
    tunnels = re.findall(r"[A-Z]{2}", line)
    flowrate = re.findall(r"\d+", line)
    flowrate = int(flowrate[0])
    active = flowrate == 0
    vertices[tunnels[0]] = (flowrate, tunnels[1:], active)

curr = "AA"
edges[curr] = bfs(curr)
poss = []

for key in vertices:
    if vertices[key][0] == 0:
        continue
    edges[key] = bfs(key)
    poss.append(key)

ugh = set()
vals = []
for _ in range(len(poss) * 2):
    # poss = poss[1:] + [poss[0]]
    random.shuffle(poss)
    if ''.join(poss) in ugh:
        continue
    ugh.add(''.join(poss))

    for i in range(1, len(poss) // 2 + 1):
        a = poss[i:]
        b = poss[:i]
        ugh.add((''.join(a), ''.join(b)))
        vals.append(rec_desc(curr, a, 26) + rec_desc(curr, b, 26))
        print(a, b, max(vals))

# print("1:", rec_desc(curr, poss, 30))
# print("2:", max(vals))
# low: 2284
# low: 2606
# low: 2711
# low: 2760
