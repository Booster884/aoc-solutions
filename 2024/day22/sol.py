from collections import deque

numbers = [int(x) for x in open("input").readlines()]
price_lists = []

MAX_NUM = 16777216

part1 = 0

for number in numbers:
    price_list = [number % 10]
    for _ in range(2000):
        number = (number ^ (number << 6)) % MAX_NUM
        number = (number ^ (number >> 5)) % MAX_NUM
        number = (number ^ (number << 11)) % MAX_NUM
        price_list.append(number % 10)
    part1 += number
    price_lists.append(price_list)

print(part1)

seq_profit = dict()

for idx, price_list in enumerate(price_lists):
    diffs = deque([], 4)
    for i in range(1, len(price_list)):
        diffs.append(price_list[i] - price_list[i - 1])
        if i >= 4:
            sequence = tuple(diffs)
            if sequence not in seq_profit:
                seq_profit[sequence] = dict()
            if idx not in seq_profit[sequence]:
                seq_profit[sequence][idx] = price_list[i]

part2 = 0

for profit in seq_profit.values():
    part2 = max(part2, sum(profit.values()))

print(part2)
