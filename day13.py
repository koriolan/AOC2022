from time import perf_counter as pfc
start = pfc()


def parse(s):
    packet = []
    tmp = ''
    appends = 0
    cur = packet
    for i in s[1:-1]:
        if i == '[':
            cur.append([])
            cur = cur[-1]
            appends += 1
        elif i == ']':
            if tmp != '':
                cur.append(int(tmp))
                tmp = ''
            cur = packet
            appends -= 1
            for a in range(appends):
                 cur = cur[-1]
        elif i == ',':
            if tmp != '':
                cur.append(int(tmp))
                tmp = ''
        else:
            tmp += i

    if tmp != '':
        cur.append(int(tmp))
    return packet


def equal(a, b):
    for tmp1, tmp2 in zip(a, b):
        if type(tmp1) is not type(tmp2):
            if type(tmp1) is list:
                tmp2 = [tmp2]
            else:
                tmp1 = [tmp1]
        if type(tmp1) is list:
            res = equal(tmp1, tmp2)
            if res is not None:
                return res
        else:
            if tmp1 != tmp2:
                return tmp1 < tmp2

    return len(b) > len(a) if len(b) != len(a) else None


pairs = []
with open('input/13.txt') as f:
    for line in f.read().split('\n\n'):
        a, b = line.split('\n')
        pairs.append((parse(a), parse(b)))


idx_2 = 1
idx_6 = 2
for a in pairs:
    for b in a:
        if equal(b, [[2]]):
            idx_2 += 1
            idx_6 += 1
        elif equal(b, [[6]]):
            idx_6 += 1

print(f'Part 1: {sum(idx for idx, pair in enumerate(pairs, 1) if equal(*pair))}')
print(f'Part 2: {idx_2*idx_6}')
print(f'time: {pfc() - start}')
