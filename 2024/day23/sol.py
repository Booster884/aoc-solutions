from collections import defaultdict

lines = open("input").read().splitlines()

adj = defaultdict(list)

for line in lines:
    a, b = line.split("-")
    adj[a].append(b)
    adj[b].append(a)

triangles = []

computers = list(adj.keys())

for i in range(len(computers)):
    for j in range(i + 1, len(computers)):
        for k in range(j + 1, len(computers)):
            if computers[j] in adj[computers[i]] \
            and computers[k] in adj[computers[i]] \
            and computers[k] in adj[computers[j]]:
                triangles.append([computers[i], computers[j], computers[k]])

part1 = 0
for triangle in triangles:
    for val in triangle:
        if val.startswith("t"):
            part1 += 1
            break
print(part1)

computers = set(computers)


def grow(clique, seen):
    todo = computers.copy()

    while len(todo) > 0:
        curr = todo.pop()

        if all(curr in adj[other] for other in clique):
            clique.append(curr)
        if set(clique) <= seen:
            return None

    return triangle


seen = set()
best = []

for triangle in triangles:
    clique = grow(triangle, seen)
    if clique is None:
        continue
    seen |= set(clique)
    if len(clique) > len(best):
        best = clique

print(",".join(sorted(best)))
