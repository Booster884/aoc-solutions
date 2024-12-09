def pretty(blocks):
    """Displays blocks like the challenge page for easy comparison."""
    s = ""
    for block in blocks:
        id = "." if block[1] == -1 else str(block[1])
        s += id * block[0]
    print(s)


def checksum(blocks):
    i = 0
    total = 0
    for block in blocks:
        size, id = block
        for _ in range(size):
            if id >= 0:
                total += i * int(id)
            i += 1
    return total


line = open("input").readline().strip()

blocks = []
id = 0
for i, c in enumerate(line):
    if i % 2 == 0:
        blocks.append((int(c), id))
        id += 1
    else:
        blocks.append((int(c), -1))

for id in reversed(range(id)):
    for i in reversed(range(len(blocks))):
        if blocks[i][1] == id:
            size = blocks[i][0]
            for j in range(0, i):
                if blocks[j][1] == -1:
                    if size == blocks[j][0]:
                        blocks[j] = blocks[i]
                        blocks[i] = (size, -1)
                        break
                    elif size < blocks[j][0]:
                        remaining_size = blocks[j][0] - size
                        blocks[j] = blocks[i]
                        blocks.insert(j+1, (remaining_size, -1))
                        blocks[i+1] = (size, -1)
                        break

# pretty(blocks)
print(checksum(blocks))
