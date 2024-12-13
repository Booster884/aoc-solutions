import sympy as sym
import re

configs = open("input").read().strip().split("\n\n")

button_re = re.compile(r"Button (?:A|B): X\+?(.*), Y\+?(.*)")
prize_re = re.compile(r"Prize: X=(.*), Y=(.*)")

part1 = 0
part2 = 0

for config in configs:
    a, b = button_re.findall(config)
    p = prize_re.findall(config)[0]
    p = sym.Matrix([int(p[0]), int(p[1])])
    big_p = p + sym.Matrix([10000000000000, 10000000000000])

    A = sym.Matrix([[int(a[0]), int(b[0])],
                    [int(a[1]), int(b[1])]])

    A_inv = A**-1

    p_ = A_inv @ p
    big_p_ = A_inv @ big_p

    if all(type(x) == sym.Integer for x in p_):
        part1 += 3 * p_[0] + p_[1]
    if all(type(x) == sym.Integer for x in big_p_):
        part2 += 3 * big_p_[0] + big_p_[1]

print(int(part1))
print(int(part2))
