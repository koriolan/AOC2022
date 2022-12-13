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


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if equal(array[j], pivot):
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def qsort(a, low, high):
    if low < high:
        pi = partition(a, low, high)
        qsort(a, low, pi - 1)
        qsort(a, pi + 1, high)


pairs = []
with open('input/13.txt') as f:
    for line in f.read().split('\n\n'):
        a, b = line.split('\n')
        pairs.append((parse(a), parse(b)))


flat_list = [item for sublist in pairs for item in sublist]
divider1 = [[2]]
divider2 = [[6]]
flat_list.append(divider1)
flat_list.append(divider2)
qsort(flat_list, 0, len(flat_list)-1)

print(f'Part 1: {sum(idx for idx, pair in enumerate(pairs, 1) if equal(*pair))}')
print(f'Part 2: {(flat_list.index(divider1)+1)*(flat_list.index(divider2)+1)}')
print(f'time: {pfc() - start}')
