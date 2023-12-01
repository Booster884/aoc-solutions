import re
file = open("in", "r")

lines = file.read().split('\n')[:-1]

var = {}

def attempt_solve(name):
    if type(var[name]) is int:
        return var[name]

    n = var[name]
    if n is None:
        return None

    a = attempt_solve(n[1])
    b = attempt_solve(n[2])

    if type(a) is int and type(b) is int:
        if n[0] == '+':
            return a + b
        elif n[0] == '-':
            return a - b
        elif n[0] == '*':
            return a * b
        elif n[0] == '/':
            return a // b

    return None

for line in lines:
    ints = [int(x) for x in re.findall(r"-?\d+", line)]
    names = re.findall(r"[a-z]{4}", line)
    operator = re.findall(r"\+|\-|\/|\*", line)
    if len(ints) == 1:
        var[names[0]] = ints[0]
    else:
        var[names[0]] = (operator[0], names[1], names[2])

print("1:", attempt_solve("root"))

var["humn"] = None
_, a, b = var["root"]
a = attempt_solve(a)
b = attempt_solve(b)

n = var["root"][1]
while True:
    if var[n] is None:
        print("2:", b)
        var["humn"] = b
        break

    x = attempt_solve(var[n][1])
    y = attempt_solve(var[n][2])

    op = var[n][0]
    known = 0

    # Is the right hand side the one with the unknown variable
    rhs = False
    if y is None:
        known = x
        n = var[n][2]
        rhs = True
    else:
        known = y
        n = var[n][1]
        rhs = False

    if op == '+':
        b -= known
    elif op == '-':
        if rhs:
            b = -b + known
        else:
            b += known
    elif op == '*':
        b //= known
    elif op == '/':
        if rhs:
            b = known // b
        else:
            b *= known
