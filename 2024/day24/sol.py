import sys


def eval(variables, key):
    val = variables[key]
    if isinstance(val, int):
        return val
    else:
        gate, a, b = val
        a, b = eval(variables, a), eval(variables, b)
        match gate:
            case "AND":
                return a & b
            case "OR":
                return a | b
            case "XOR":
                return a ^ b
            case _:
                raise ValueError("Unknown gate")


input_lines, gate_lines = open("input").read().split("\n\n")

variables = dict()

for line in input_lines.splitlines():
    name, value = line.split(": ")
    variables[name] = int(value)

for line in gate_lines.splitlines():
    a, gate, b, _, out = line.split()
    a, b = sorted([a, b])
    variables[out] = (gate, a, b)

swaps = [
    ("z23", "bks"),
    ("z16", "tdv"),
    ("z09", "hnd"),
    ("tjp", "nrn"),
]

for swap in swaps:
    a, b = swap
    a_gate, b_gate = variables[a], variables[b]
    variables[b] = a_gate
    variables[a] = b_gate

outputs = sorted(x for x in variables if x.startswith("z"))
print("// ", end="")  # To not break `dot` for part 2
print(sum(eval(variables, x) << i for i, x in enumerate(outputs)))

inv = {v: k for k, v in variables.items()}

# Put swaps here after finding them manually (see comment below).
# My results are not committed for obvious reasons.
swaps = []

for swap in swaps:
    a, b = swap
    a_gate, b_gate = variables[a], variables[b]
    variables[b] = a_gate
    variables[a] = b_gate


def get(gate, a, b):
    global inv
    a, b = sorted([a, b])
    return inv[(gate, a, b)]


# Automatically find swap's approximate location, and then find the actual swap
# in the graph. If the input does have the shape of a half/full adder, the code
# below will let you know with either an `AssertionError` or a `KeyError`.

carry = None
for i in range(len(outputs) - 1):
    if i == 0:
        # Half adder
        assert get("XOR", "x00", "y00") == "z00"
        carry = get("AND", "x00", "y00")
    else:
        # Full adder
        i_fmt = str(i).zfill(2)
        x, y, z = f"x{i_fmt}", f"y{i_fmt}", f"z{i_fmt}"
        a = get("XOR", x, y)
        c = get("AND", x, y)
        assert get("XOR", a, carry) == z

        b = get("AND", a, carry)
        carry = get("OR", b, c)

if len(swaps) > 0:
    a, b = list(zip(*swaps))
    print("// ", end="")  # To not break `dot` below
    print(",".join(sorted(list(a) + list(b))))

# Why compute when you can just look at a graph?!
# python sol.py draw | dot -Tsvg -o circuit.svg

try:
    if not sys.argv[1] == "draw":
        exit()
except IndexError:
    exit()

print("graph circuit {")

i = 0
for key, val in variables.items():
    if not isinstance(val, int):
        gate, a, b = val

        print(f"    {a} -- {gate}{i};")
        print(f"    {b} -- {gate}{i};")
        print(f"    {gate}{i} -- {key};")
        i += 1

print("}")
