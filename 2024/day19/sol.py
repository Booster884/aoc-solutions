from functools import cache

patterns, designs = open("input").read().strip().split("\n\n")
patterns = sorted(patterns.split(", "), key=len)
designs = designs.splitlines()

@cache
def combinations(s):
    if s == "":
        return 1
    comb = 0
    for pattern in patterns:
        if s.startswith(pattern):
            comb += combinations(s[len(pattern):])
    return comb

part1 = 0
part2 = 0
for design in designs:
    comb = combinations(design)
    if comb > 0:
        part1 += 1
    part2 += comb

print(part1)
print(part2)
