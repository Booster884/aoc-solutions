with open('in') as f:
    route, nodes_ = f.read().split('\n\n')

nodes = {}
for node in nodes_.strip().split('\n'):
    node, edges = node.split(' = ')
    left, right = edges[1:-1].split(', ')
    nodes[node] = (left, right)

curr = 'AAA'
i = 0
while True:
    curr = nodes[curr][route[i % len(route)] == 'R']
    if curr == 'ZZZ':
        break
    i += 1

print('1:', i + 1)
