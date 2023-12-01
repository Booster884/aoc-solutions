from functools import cmp_to_key
file = open("in", "r")

s = 0
l = []

def cmp(l0, l1):
    i = 0
    # while len(l0) > 0 and len(l1) > 0:
    while i < len(l0) and i < len(l1):
        a = l0[i]
        b = l1[i]
        if type(a) == type(b) == int:
            if a < b:
                return True
            elif a > b:
                return False
        elif type(a) == type(b) == list:
            c = cmp(a, b)
            if c != None:
                return c
        else:
            if type(a) == int:
                a = [a]
            else:
                b = [b]

            c = cmp(a, b)
            if c != None:
                return c
        i += 1

    if len(l0) > len(l1):
        return False
    elif len(l0) < len(l1):
        return True

    return None

def cmp_int(a, b):
    c = cmp(a, b)
    if c == True:
        return -1
    elif c == False:
        return 1
    else:
        return 0

for i, line in enumerate(file.read().split('\n')[:-1]):
    if line == '':
        continue
    l.append(eval(line))

l.append([[2]])
l.append([[6]])

l.sort(key=cmp_to_key(cmp_int))

print("1:", s)
print("2:", (l.index([[2]]) + 1) * (l.index([[6]]) + 1))
