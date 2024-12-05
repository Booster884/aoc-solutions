from collections import defaultdict

with open("input") as f:
    inp = f.read()

orderings, updates = inp.split("\n\n")
orderings, updates = orderings.splitlines(), updates.splitlines()

# Map from page numbers to a set of page numbers that must come before
priors = defaultdict(set)

for ordering in orderings:
    before, after = ordering.split("|")
    priors[after].add(before)

part1 = 0
part2 = 0

for update in updates:
    seen = set()
    valid = True
    items = update.split(",")
    for item in items:
        if not seen <= priors[item]:
            valid = False
        seen.add(item)
    if valid:
        part1 += int(items[len(items)//2])
    else:
        # Reorder
        order = []
        pages = set(items)
        while len(pages) > 0:
            for page in pages:
                if len(priors[page] & pages) == 0:
                    order.append(page)
                    pages.remove(page)
                    break
        part2 += int(order[len(items)//2])

print(part1)
print(part2)
