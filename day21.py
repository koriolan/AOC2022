from time import perf_counter as pfc

start = pfc()
monkeys = {}
unresolved = set()
with open('input/21.txt') as f:
    operations = {'+': float.__add__, '-': float.__sub__, '*': float.__mul__, '/': float.__truediv__}
    for l in f.readlines():
        name, operation = l.strip().split(':')
        sp = operation.strip(' ').split(' ')
        if len(sp) == 1:
            monkeys[name] = float(sp[0])
        else:
            monkeys[name] = None
            unresolved.add((name, sp[0], sp[2], operations[sp[1]]))


def why(apes, un, part2):
    if part2:
        apes['humn'] = None

    while apes['humn' if part2 else 'root'] is None:
        tmp = set()
        for n, a, b, o in un:
            if apes[a] is not None and apes[b] is not None:
                apes[n] = o(apes[a], apes[b])
            else:
                tmp.add((n, a, b, o))
        if tmp == un:
            return tmp
        un = tmp
    return apes['humn' if part2 else 'root']


ap = monkeys.copy()
humn = why(ap, unresolved, True)
resh = set()
for n, a, b, o in humn:
    if n != 'root':
        if o == float.__mul__:
            resh.add((a, n, b, float.__truediv__))
            resh.add((b, n, a, float.__truediv__))
        elif o == float.__add__:
            resh.add((a, n, b, float.__sub__))
            resh.add((b, n, a, float.__sub__))
        elif o == float.__sub__:
            resh.add((a, n, b, float.__add__))
            resh.add((b, a, n, float.__sub__))
        else:
            resh.add((a, n, b, float.__mul__))
            resh.add((b, a, n, float.__truediv__))
    else:
        if ap[a] is None:
            ap[a] = ap[b]
        else:
            ap[b] = ap[a]
part2 = why(ap, resh, True)
part1 = why(monkeys.copy(), unresolved, False)
print(f'part 1: {part1}')
print(f'part 2: {part2}')
print(f'time: {pfc() - start}')
