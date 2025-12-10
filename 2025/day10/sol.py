from collections import deque

with open("input") as f:
    inp = f.read()

# inp = """
# [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
# [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
# [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
# """

p1 = 0
for line in inp.strip().splitlines():
    elems = line.split()
    bin_goal = [b == '#' for b in elems[0][1:-1]]
    dec_goal = [int(x) for x in elems[-1][1:-1].split(',')]
    buttons = [[int(a) for a in x[1:-1].split(',')] for x in elems[1:-1]]

    q = deque()
    q.append(([False] * len(bin_goal), 0))

    while len(q) > 0:
        (curr, n) = q.popleft()
        if bin_goal == curr:
            p1 += n
            break
        for button in buttons:
            new = curr[:]
            for i in button:
                new[i] = not new[i]
            q.append((new, n + 1))

print(p1)
