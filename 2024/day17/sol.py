regs, instrs = open("input").read().strip().split("\n\n")

regs = [int(line.split(": ")[1]) for line in regs.splitlines()]
instrs = [int(x) for x in instrs.split(": ")[1].split(",")]

def combo(opcode: int, regs) -> int:
    if opcode <= 3:
        return opcode
    elif opcode <= 6:
        return regs[opcode - 4]
    else:
        raise ValueError

def run(regs, instrs):
    ip = 0
    output = []

    while ip < len(instrs):
        instr = instrs[ip]
        opcode = instrs[ip + 1]
        # print(instr, opcode, [oct(x) for x in regs])

        match instr:
            case 0:
                # regs[0] = regs[0] // 2**combo(opcode, regs)
                regs[0] = regs[0] >> combo(opcode, regs)
            case 1:
                regs[1] ^= opcode
            case 2:
                regs[1] = combo(opcode, regs) % 8
            case 3:
                if regs[0] != 0:
                    ip = opcode
                    continue
            case 4:
                regs[1] ^= regs[2]
            case 5:
                output.append(combo(opcode, regs) % 8)
            case 6:
                # regs[1] = regs[0] // 2**combo(opcode, regs)
                regs[1] = regs[0] >> combo(opcode, regs)
            case 7:
                # regs[2] = regs[0] // 2**combo(opcode, regs)
                regs[2] = regs[0] >> combo(opcode, regs)

        ip += 2

    return output

part1 = run(regs, instrs)
print(','.join(str(x) for x in part1))

# General form of the program seems to be as follows:
# - Pop last 3 bits (octal digit) off the number in A into B;
# - Do some math (possibly dependent on rest of A);
# - Output last 3 bits (octal digit) of B to string.
#
# Now we do that in reverse, by adding 3 bits to a number until it matches the
# end of the instructions and looking further.

stack = [(0, 0)]
possible = []
while len(stack) > 0:
    curr, idx = stack.pop()
    if idx == len(instrs):
        possible.append(curr)
    for i in range(8):
        if run([(curr << 3) + i, 0, 0], instrs) == instrs[-idx-1:]:
            stack.append(((curr << 3) + i, idx + 1))

print(min(possible))
