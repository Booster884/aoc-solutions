from queue import PriorityQueue

# ENWS
dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

grid = open("input").readlines()

start = (0, 0)
end = (0, 0)
maze = set()
for y, row in enumerate(grid):
    for x, c in enumerate(row):
        if c != "#":
            maze.add((x, y))
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)


def dijkstra(maze, start, end):
    frontier = PriorityQueue()
    frontier.put((0, start, 0, []))
    seen = dict()

    while not frontier.empty():
        score, pos, dir, path = frontier.get()
        x, y = pos

        # LHS of and is not necessary (???)
        if (pos, dir) in seen:
            continue
        seen[(pos, dir)] = score

        if pos == end:
            return score, path

        dx, dy = dirs[dir]
        next = (x + dx, y + dy)
        if next in maze:
            frontier.put((score + 1, next, dir, path + [next]))
        frontier.put((score + 1000, pos, (dir + 1) % 4, path))
        frontier.put((score + 1000, pos, (dir - 1) % 4, path))

    return 0, []


score, path = dijkstra(maze, start, end)
print(score)

on_same_score = set(path) | set([start])

for pos in path:
    assert maze != (maze - set([pos]))
    s, p = dijkstra(maze - set([pos]), start, end)
    if s == score:
        on_same_score |= set(p)

print(len(on_same_score))
