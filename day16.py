import functools
import sys
from time import perf_counter as pfc

start = pfc()
verticles = {}
pumps = {}
pumps_works = []

with open('input/16.txt') as f:
    for line in f.readlines():
        v, p, *t = line.strip().replace('Valve ', '').replace(' has flow rate=', ',').replace('; tunnels lead to valves ', ',')\
            .replace('; tunnel leads to valve ', ',').replace(' ','').split(',')
        verticles[v] = t
        pumps[v] = int(p)
        if pumps[v] > 0:
            pumps_works.append(v)


w = dict()

for i in pumps:
    w[i, i] = 0

for v, edge in verticles.items():
    for e in edge:
        w[v, e] = 1

for k in pumps:
    for i in pumps:
        for j in pumps:
            w[i, j] = min(w.get((i, j), sys.maxsize), w.get((i, k), sys.maxsize) + w.get((k, j), sys.maxsize))


@functools.cache
def find(ost, st, p, e):
    max_pressure = find(26, 'AA', p, False) if e else 0
    for i in p:
        o = ost - (w[st, i]+1)
        t = 0
        if o > 0:
            t = o*pumps[i]+find(o, i, p-{i}, e)
        if t > max_pressure:
            max_pressure = t
    return max_pressure


part1 = find(30, 'AA', frozenset(pumps_works), False)
part2 = find(26, 'AA', frozenset(pumps_works), True)

print(f'Part 1:{part1}')
print(f'Part 1:{part2}')
print(f'time: {pfc() - start}')