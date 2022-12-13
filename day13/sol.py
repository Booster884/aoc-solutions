file = open("in", "r")

s = 0
l = []

def cmp(l0, l1):
    while len(l0) > 0 and len(l1) > 0:
        a = l0.pop(0)
        b = l1.pop(0)
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
    if len(l0) > len(l1):
        return False
    elif len(l0) < len(l1):
        return True

    return None


for i, pair in enumerate(file.read().split('\n\n')):
    left, right = pair.strip().split('\n')
    left = eval(left)
    right = eval(right)
    # print(cmp(left, right))
    if cmp(left, right):
        print(i + 1)
        s += i + 1
    # print(left)

# True
# True
# False
# True
# False
# True
# False
# False

print("1:", s)
print("2:")

# 3174 low
# 4201 low
# 5768 high
