file = open("in", "r")

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

line = file.read().split('\n')[0]
jets = [-1 if c == '<' else 1 for c in line]

rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],         # -
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)], # +
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)], # J
    [(0, 0), (0, 1), (0, 2), (0, 3)],         # |
    [(0, 0), (0, 1), (1, 0), (1, 1)]          # o
]

rock_i = 0
jet_i = 0
old_stack_height = 0
stack_height = 0
width = 7
landed = set()
hah = {}
gaming = False
stack_height_offset = 0

end = 2022
# end = 1000000000000

while rock_i < end:
    rock = rocks[rock_i % len(rocks)].copy()
    pos = (2, stack_height + 3)
    for i, tile in enumerate(rock):
        rock[i] = (tile[0] + pos[0], tile[1] + pos[1])

    if (rock_i % len(rocks), jet_i % len(jets)) in hah and not gaming:
        bruh = hah[(rock_i % len(rocks), jet_i % len(jets))]
        cycle_len = rock_i - bruh[2]
        n = (end - rock_i) // cycle_len
        # print(hah)
        height_d = stack_height - bruh[0]
        jet_d = jet_i - bruh[1]
        rock_d = rock_i - bruh[2]
        print(height_d, jet_d, rock_d)
        stack_height_offset = height_d * n
        jet_i += jet_d * n
        rock_i += rock_d * n
        print(stack_height, jet_i, rock_i)
        gaming = True
    else:
        bruh = (stack_height, jet_i, rock_i)
        hah[(rock_i % len(rocks), jet_i % len(jets))] = bruh

    grounded = False
    while not grounded:
        # Push
        jet = jets[jet_i % len(jets)]
        jet_i += 1
        can_move = True
        for tile in rock:
            if not (-1 < tile[0] + jet < width):
                can_move = False
                break
            elif (tile[0] + jet, tile[1]) in landed:
                can_move = False
                break
        if can_move:
            for i, tile in enumerate(rock):
                rock[i] = (tile[0] + jet, tile[1])

        # Fall
        can_fall = True
        for tile in rock:
            if tile[1] - 1 < 0 or (tile[0], tile[1] - 1) in landed:
                can_fall = False
                break
        if can_fall:
            for i, tile in enumerate(rock):
                rock[i] = (tile[0], tile[1] - 1)
        else:
            for tile in rock:
                landed.add(tile)
            for y in range(stack_height, stack_height + 10):
                for x in range(width):
                    if (x, y) in landed:
                        stack_height = y + 1
            grounded = True

    rock_i += 1

# start_y = 49
# for y in range(start_y + 40, start_y - 1, -1):
#     line = ''
#     for x in range(width):
#         line += '#' if (x, y) in landed else '.'
#     print(line, y)
# print("0123456\n")

# s = ''
# for y in range(stack_height):
#     for x in range(width):
#         s += '#' if (x, y) in landed else '.'
#     s += '|'
#
# print(hah, len(hah))

print("1:", stack_height + stack_height_offset)
print("2:", 2)

# 1548973607043 is too low
