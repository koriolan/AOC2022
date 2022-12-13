from time import perf_counter as pfc
start = pfc()


def parse(s):
    packet = []
    tmp = ''
    appends = []
    for i in s[1:-1]:
        if i == '[':
            t = packet
            for a in appends:
                t = t[a]
            t.append([])
            appends.append(-1)
        elif i == ']':
            if tmp != '':
                t = packet
                for a in appends:
                    t = t[a]
                t.append(int(tmp))
                tmp = ''
            appends.pop()
        elif i == ',':
            if tmp != '':
                t = packet
                for a in appends:
                    t = t[a]
                t.append(int(tmp))
                tmp = ''
        else:
            tmp += i

    if tmp != '':
        t = packet
        for a in appends:
            t = t[a]
        t.append(int(tmp))
    return packet


def equal(a, b):
    for idx, i in enumerate(a):
        if idx >= len(b):
            return False
        if type(i) is list:
            tmp = b[idx]
            if type(tmp) is not list:
                tmp = [b[idx]]
            res = equal(i, tmp)
            if res is not None:
                return res
        elif type(b[idx]) is list:
            tmp = i
            if type(tmp) is not list:
                tmp = [i]
            res = equal(tmp, b[idx])
            if res is not None:
                return res
        else:
            if i > b[idx]:
                return False
            elif i < b[idx]:
                return True
    if len(b) > len(a):
        return True
    return None


pairs = []
with open('input/13.txt') as f:
    for line in f.read().split('\n\n'):
        a, b = line.split('\n')
        pairs.append((parse(a), parse(b)))


min_2 = 1
min_6 = 2
for a, b in pairs:
    if equal(a, [[2]]):
        min_2 += 1
    if equal(a, [[6]]):
        min_6 += 1
    if equal(b, [[2]]):
        min_2 += 1
    if equal(b, [[6]]):
        min_6 += 1

print(f'Part 1: {sum(idx for idx, pair in enumerate(pairs, 1) if equal(*pair))}')
print(f'Part 2: {min_2*min_6}')
print(f'time: {pfc() - start}')
