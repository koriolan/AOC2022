from time import perf_counter as pfc

start = pfc()
d = {'1': 1, '2': 2, '0': 0, '=': -2, '-': -1, 0: '0', 1: '1', 2: '2', 3: '=', 4: '-', 5: '0'}

with open('input/25.txt') as f:
    part1_10 = sum([sum([d[s[i]] * 5 ** (-i - 2) for i in range(-2, -len(s) - 1, -1)]) for s in f.readlines()])

part1 = ''
per = 0
while part1_10 > 0:
    ost = part1_10 % 5 + per
    part1_10 //= 5
    per = ost // 3
    part1 = d[ost] + part1

print(f'Part 1: {part1}')
print(f'time: {pfc() - start}')
