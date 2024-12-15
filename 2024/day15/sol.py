dirs = {
    "^": (0, -1),
    "v": (0, 1),
    "<": (-1, 0),
    ">": (1, 0),
}

def show_grid():
    for y in range(h):
        for x in range(w):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("O", end="")
            elif (x, y) == robot:
                print("@", end="")
            else:
                print(".", end="")
        print()
    print()

def score_grid():
    return sum(y * 100 + x for x, y in boxes)

grid, instrs = open("input").read().strip().split("\n\n")

grid = grid.splitlines()
walls = set()
robot = (0, 0)
boxes = set()
w, h = len(grid[0]), len(grid)

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        match c:
            case "#":
                walls.add((x, y))
            case "O":
                boxes.add((x, y))
            case "@":
                robot = (x, y)
            case _:
                pass

for instr in instrs:
    if instr == "\n":
        continue
    dx, dy = dirs[instr]
    x, y = robot
    nx, ny = x + dx, y + dy
    if (nx, ny) in walls:
        pass
    elif (nx, ny) in boxes:
        ex, ey = nx + dx, ny + dy
        while True:
            if (ex, ey) in walls:
                # No space to move row boxes
                break
            elif (ex, ey) in boxes:
                # More boxes after, continue looking.
                ex, ey = ex + dx, ey + dy
            else:
                # space is empty, can move row of boxes.
                boxes.remove((nx, ny))
                boxes.add((ex, ey))
                robot = (nx, ny)
                break
    else:
        robot = (nx, ny)

show_grid()
print(score_grid())
