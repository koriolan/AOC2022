from time import perf_counter as pfc
start = pfc()

def find(cnt):
    with open('input/6.txt') as f:
        key = f.read(cnt)
        for l in f.read():
            if len(set(key[-cnt:])) == cnt:
                break
            else:
                key += l
    return len(key)


print(f'part 1: {find(4)}')
print(f'part 2: {find(14)}')
print(f'time: {pfc() - start}')
