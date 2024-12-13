import numpy as np
import re

configs = open("test").read().strip().split("\n\n")

button_re = re.compile(r"Button (?:A|B): X\+?(.*), Y\+?(.*)")
prize_re = re.compile(r"Prize: X=(.*), Y=(.*)")

part1 = 0
part2 = 0

for config in configs:
    a, b = button_re.findall(config)
    p = prize_re.findall(config)[0]
    a = np.array([[float(a[0])], [float(a[1])]])
    b = np.array([[float(b[0])], [float(b[1])]])
    p = np.array([[float(p[0])], [float(p[1])]])
    big_p = p + np.array([[10000000000000], [10000000000000]])

    A = np.hstack((a, b))
    A_inv = np.linalg.inv(A)

    p_ = A_inv @ p
    big_p_ = A_inv @ big_p

    if np.allclose(p_, np.round(p_)):
        part1 += np.sum(p_ * np.array([[3], [1]]))
    if np.allclose(big_p_, np.round(big_p_)):
        print(big_p_)
        part2 += int(np.sum(big_p_ * np.array([[3], [1]])))

print(int(part1))
# This is not correct due to floating point error.
print(int(part2))
