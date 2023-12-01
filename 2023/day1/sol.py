with open('input') as f:
    lines = f.readlines()

# Part 1
# ans = 0
# for line in lines:
#     nums = [char for char in line if char.isdigit()]
#     ans += int(nums[0] + nums[-1])
# print(ans)

# Part 2
import re

# Should've indexed an array
mapping = {
    '0': 0,
    '1': 1, 'one': 1,
    '2': 2, 'two': 2,
    '3': 3, 'three': 3,
    '4': 4, 'four': 4,
    '5': 5, 'five': 5,
    '6': 6, 'six': 6,
    '7': 7, 'seven': 7,
    '8': 8, 'eight': 8,
    '9': 9, 'nine': 9,
}

ans = 0
for line in lines:
    # Numbers can overlap; first time I've used /(?=...)/
    pattern = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"
    nums = [mapping[num] for num in re.findall(pattern, line)]
    ans += int(nums[0] * 10 + nums[-1])
print(ans)

