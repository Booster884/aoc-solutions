from functools import reduce
from operator import mul

file = open("in", "r")

monkeys = []

for inp in file.read().split('\n\n'):
    monkey = []
    for line in inp.split('\n')[1:]:
        line = line.strip().split()

        if len(line) == 0:
            continue

        if line[0] == "Starting":
            monkey.append([int(x.replace(',','')) for x in line[2:]])
        elif line[0] == "Operation:":
            monkey.append(" ".join(line[3:]))
        elif line[0] == "Test:":
            monkey.append(int(line[-1]))
        elif line[1] == "true:":
            monkey.append(int(line[-1]))
        elif line[1] == "false:":
            monkey.append(int(line[-1]))
    monkeys.append(monkey)

inspects = [0] * len(monkeys)

gcd = reduce(mul, [monkey[2] for monkey in monkeys], 1)

# for i in range(20):
for i in range(10000):
    for n, monkey in enumerate(monkeys):
        while len(monkey[0]) > 0:
            inspects[n] += 1
            old = monkey[0].pop()
            # new = int(eval(monkey[1]))//3
            new = int(eval(monkey[1])) % gcd
            if new % monkey[2] == 0:
                monkeys[monkey[3]][0].append(new)
            else:
                monkeys[monkey[4]][0].append(new)

inspects.sort()
print(inspects[-1] * inspects[-2])
