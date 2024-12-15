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
                print("[", end="")
            elif (x-1, y) in boxes:
                print("]", end="")
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
w, h = len(grid[0])*2, len(grid)

for y, row in enumerate(grid):
    for x, c in enumerate(row):
        match c:
            case "#":
                walls.add((2*x, y))
                walls.add((2*x+1, y))
            case "O":
                boxes.add((x*2, y))
            case "@":
                robot = (x*2, y)
            case _:
                pass

show_grid()

def collide_wide(x, y, ignore_pos=None):
    if (x, y) in boxes:
        if (x, y) == ignore_pos:
            return None
        return (x, y)
    elif (x - 1, y) in boxes:
        if (x - 1, y) == ignore_pos:
            return None
        return (x - 1, y)
    return None

def can_move(box, dir):
    if box == None:
        return True
    dx, dy = dir
    bx, by = box

    if (bx + dx, by + dy) in walls or (bx + dx + 1, by + dy) in walls:
        return False

    box0 = collide_wide(bx + dx, by + dy, box)
    box1 = collide_wide(bx + dx + 1, by + dy, box)
    if not any([box0, box1]):
        # Nothing preventing movement
        return True

    move_succes = [can_move(b, dir) for b in [box0, box1] if b is not None]

    return all(move_succes)

def move(box, dir):
    if box == None:
        return True
    dx, dy = dir
    bx, by = box

    if (bx + dx, by + dy) in walls or (bx + dx + 1, by + dy) in walls:
        return False

    box0 = collide_wide(bx + dx, by + dy, box)
    box1 = collide_wide(bx + dx + 1, by + dy, box)

    for b in set([box0, box1]):
        move(b, dir)

    boxes.remove(box)
    boxes.add((bx + dx, by + dy))

for instr in instrs:
    if instr == "\n":
        continue
    print(instr)
    dx, dy = dirs[instr]
    x, y = robot
    nx, ny = x + dx, y + dy
    if (nx, ny) in walls:
        pass
    elif box := collide_wide(nx, ny):
        if can_move(box, (dx, dy)):
            move(box, (dx, dy))
            robot = (nx, ny)
    else:
        robot = (nx, ny)

show_grid()
print(score_grid())
