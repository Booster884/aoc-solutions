from math import lcm


with open('in') as f:
    route, nodes_ = f.read().split('\n\n')

nodes = {}
for node in nodes_.strip().split('\n'):
    node, edges = node.split(' = ')
    left, right = edges[1:-1].split(', ')
    nodes[node] = (left, right)

curr = [node for node in nodes.keys() if node[-1] == 'A']
loop_lengths = [0] * len(curr)

i = 0
while True:
    for j, c in enumerate(curr):
        curr[j] = nodes[c][route[i % len(route)] == 'R']
        if curr[j][-1] == 'Z':
            loop_lengths[j] = i + 1
    if all([l != 0 for l in loop_lengths]):
        break

    i += 1

print('2:', lcm(*loop_lengths))
