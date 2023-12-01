import re
file = open("test", "r")

lines = file.read().split('\n')[:-1]

# def rec(resources, robots, costs, time_left):
#     print(time_left, resources)
#     if time_left == 0:
#         return resources[-1]
#
#     # Collect resources
#     for i in range(len(robots)):
#         resources[i] += robots[i]
#
#     poss = []
#     # Check all possibilities for buying robots
#     for i in range(len(costs)):
#         can_buy = all([resources[j] >= costs[i][j] for j in range(len(costs[i]))])
#         if not can_buy:
#             continue
#         robots_ = robots[:]
#         resources_ = resources[:]
#         robots_[i] += 1
#         resources_[i] += 1
#         for j in range(len(costs[i])):
#             resources_[j] -= costs[i][j]
#         a = rec(resources_, robots_, costs, time_left - 1)
#         poss.append(a)
#
#
#     # Buy nothing?
#     a = rec(resources[:], robots[:], costs, time_left - 1)
#     poss.append(a)
#     print(poss)
#
#     return resources[-1]

for line in lines:
    # print(line.split(". "))
    ints = [int(x) for x in re.findall(r"-?\d+", line)]
    
    ore_cost = (ints[1], 0, 0, 0)
    clay_cost = (ints[2], 0, 0, 0)
    obsidian_cost = (ints[3], ints[4], 0, 0)
    geode_cost = (ints[5], 0, ints[6], 0)
    costs = [ore_cost, clay_cost, obsidian_cost, geode_cost]
    print(costs)

    resources = [0, 0, 0, 0]
    robots = [1, 0, 0, 0]

    seen = set()
    complete = []
    stack = []
    stack.append((resources[:], robots[:], 24))

    uh = 0
    while len(stack) > 0:
        # uh += 1
        # if uh > 1000000:
        #     break
        resources, robots, time = stack.pop()
        if time <= 0:
            complete.append((resources[:], robots[:], time))
            # complete.append(resources[:])
            continue

        for i in range(len(costs)):
            can_buy = all([resources[j] >= costs[i][j] for j in range(len(costs[i]))])
            if not can_buy:
                continue

            _robots = robots[:]
            _robots[i] += 1
            _resources = resources[:]
            for j in range(len(costs[i])):
                _resources[j] -= costs[i][j]

            hah = (tuple(_resources), tuple(_robots), time - 1)
            if hah in seen:
                continue
            seen.add(hah)

            stack.append((_resources, _robots, time - 1))

        for i in range(len(robots)):
            resources[i] += robots[i]

        stack.append((resources[:], robots[:], time - 1))

        # print(resources, robots, time)

    # print(complete)
    # for x in complete:
    #     print(x[1])
    # print([1, 4, 2, 2] in complete[1])
    print(max([c[1][-1] for c in complete]))
    geodes = [c[0][-1] for c in complete]
    print(max(geodes))

    # rec([1, 0, 0, 0], [1, 0, 0, 0], costs, 26)
    # print(geode_cost)

print("1:", 1)
print("2:", 2)
