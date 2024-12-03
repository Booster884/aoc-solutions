import re

with open("input") as f:
    inp = f.read()

pattern = re.compile(r"mul\((\d+),(\d+)\)")
pairs = pattern.findall(inp)
print(sum(map(lambda a, b: int(a) * int(b), *zip(*pairs))))

pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
tuples = pattern.findall(inp)

total = 0
working = True
for a, b, do, dont in tuples:
    if do != '':
        working = True
    elif dont != '':
        working = False
    elif working:
        total += int(a) * int(b)
print(total)
