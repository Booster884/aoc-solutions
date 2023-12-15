from collections import defaultdict

with open('in') as f:
    steps = f.read().strip().split(',')

def hash(string):
    value = 0
    for c in string:
        value = (value + ord(c)) * 17 % 256
    return value


hash_table = defaultdict(list)
for step in steps:
    if step.endswith('-'):
        label = step.strip('-')
        h = hash(label)
        hash_table[h] = [(k, v) for (k, v) in hash_table[h] if k != label]
    else:
        label, value = step.split('=')
        h = hash(label)
        smae_label = [(k, v) for (k, v) in hash_table[h] if k == label]
        if len(smae_label) > 0:
            hash_table[h] = [(k, value) if k == label else (k, v) for (k, v) in hash_table[h]]
        else:
            hash_table[h].append((label, value))

ans2 = 0
for k, v in hash_table.items():
    for i, (_, f) in enumerate(v):
        ans2 += (k + 1) * (i + 1) * int(f)

print('1:', sum(hash(step) for step in steps))
print('2:', ans2)
