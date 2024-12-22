numbers = [int(x) for x in open("input").readlines()]

MAX_NUM = 16777216

part1 = 0

for number in numbers:
    for _ in range(2000):
        number = (number ^ (number << 6)) % MAX_NUM
        number = (number ^ (number >> 5)) % MAX_NUM
        number = (number ^ (number << 11)) % MAX_NUM
    part1 += number

print(part1)
