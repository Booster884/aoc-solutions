from lark import Lark

with open('in') as f:
    raw_rules, raw_parts = f.read().strip().split('\n\n')
    part_parser = Lark('''start: "{" (pair ",")* pair? "}"
                          pair: ID "=" VALUE
                          ID: "x" | "m" | "a" | "s"
                          VALUE: ("0".."9")+
                       ''')

    parts = []
    for raw_part in raw_parts.split('\n'):
        part_tree = part_parser.parse(raw_part)
        values = [int(part.children[1].value) for part in part_tree.children]
        parts.append(values)

    rule_parser = Lark('''start: NAME "{" (workflow ",")* NAME "}"
                          workflow: ID OP VALUE ":" NAME
                          OP: ">" | "<"
                          ID: "x" | "m" | "a" | "s"
                          NAME: ("a".."z")+
                          VALUE: ("0".."9")+
                       ''')

    rules = {}
    for raw_rule in raw_rules.split('\n'):
        rule_tree = rule_parser.parse(raw_rule)
        name, *workflow_trees, default = rule_tree.children
        workflows = []
        for tree in workflow_trees:
            i, o, v, n = map(lambda token: token.value, tree.children)
            workflows.append((i, o, int(v), n))
        rules[name.value] = workflows + [default.value]

key = 'xmas'
ans1 = 0

for part in parts:
    curr = 'in'

    while True:
        if curr == 'A':
            ans1 += sum(part)
            break
        elif curr == 'R':
            break

        for i, o, v, n in rules[curr][:-1]:
            if o == '>' and part[key.index(i)] > v:
                curr = n
                break
            elif o == '<' and part[key.index(i)] < v:
                curr = n
                break
        else:
            curr = rules[curr][-1]

print('1:', ans1)
