with open('in') as f:
    lines = f.readlines()

def get_groups(record: str):
    groups = []
    group = 0
    for c in record:
        if c == '.':
            if group != 0:
                groups.append(group)
            group = 0
        else:
            group += 1
    if group != 0:
        groups.append(group)
    return groups

def solve(record: str, groups: list[int]) -> int:
    for i, c in enumerate(record):
        if c == '?':
            r = 0
            r += solve(f"{record[:i]}#{record[i+1:]}", groups)
            r += solve(f"{record[:i]}.{record[i+1:]}", groups)
            return r
    else:
        return int(get_groups(record) == groups)

ans1 = 0
for line in lines:
    record, groups = line.split()
    groups = [int(x) for x in groups.split(',')]
    ans1 += solve(record, groups)

print('1:', ans1)
