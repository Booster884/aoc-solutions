import re
file = open("in", "r")

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

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
        # print(press, time_left)
        return press * time_left

    a = []
    for n in paths_left:
        next_paths = paths_left.copy()
        next_paths.remove(n)
        # print(n, next_paths)
        a.append(rec_desc(n, next_paths, time_left - 1 - edges[curr][n]))

    press = vertices[curr][0]
    return press * time_left + max(a)


for line in lines:
    tunnels = re.findall(r"[A-Z]{2}", line)
    flowrate = re.findall(r"\d+", line)
    flowrate = int(flowrate[0])
    active = flowrate == 0
    vertices[tunnels[0]] = (flowrate, tunnels[1:], active)
# print(vertices)

curr = "AA"
edges[curr] = bfs(curr)
poss = []

for key in vertices:
    if vertices[key][0] == 0:
        continue
    edges[key] = bfs(key)
    poss.append(key)

print("1:", rec_desc(curr, poss, 30))
print("2:", 2)
