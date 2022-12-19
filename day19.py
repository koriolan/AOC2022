import functools
from time import perf_counter as pfc

start = pfc()


blueprints = set()
i = 1
with open('input/19.txt') as f:
    for line in f.readlines():
        costs = line.strip().replace('.', '').split(' ')
        blueprints.add((int(costs[6]), int(costs[12]), (int(costs[18]), int(costs[21])), (int(costs[27]), int(costs[30])), i))
        i += 1


@functools.cache
def step(cnt, robots, solid, blueprint):
    if cnt == 1:
        return tuple(i for i in map(sum, zip(solid, robots)))
    maybe = [((0, 0, 0, 0), (0, 0, 0, 0))]
    if blueprint[3][0] <= solid[0] and blueprint[3][1] <= solid[2]:
        maybe = [((0, 0, 0, 1), (-blueprint[3][0], 0, -blueprint[3][1], 0))]
    elif blueprint[2][0] <= solid[0] and blueprint[2][1] <= solid[1]:
        maybe = [((0, 0, 1, 0), (-blueprint[2][0], -blueprint[2][1], 0, 0))]
    else:
        if blueprint[0] <= solid[0]:
            maybe.append(((1, 0, 0, 0), (-blueprint[0], 0, 0, 0)))
        if blueprint[1] <= solid[0]:
            maybe.append(((0, 1, 0, 0), (-blueprint[1], 0, 0, 0)))

    max_geodes = [-1, -1, -1, -1]
    for r, s in maybe:
        t = step(cnt-1, tuple(i for i in map(sum, zip(robots, r))), tuple(i for i in map(sum, zip(solid, robots, s))), blueprint)
        if t[3] > max_geodes[3]:
            max_geodes = t
    return max_geodes


part1 = 0
for b in blueprints:
    tmp = (step(24, (1, 0, 0, 0), (0, 0, 0, 0), b), b[-1])
    step.cache_clear()
    part1 += tmp[-1] * tmp[0][-1]

print(f'Part 1: {part1}')
print(f'time: {pfc() - start}')

start = pfc()
part2 = 1
for b in blueprints:
    if b[-1] in [1, 2, 3]:
        tmp = (step(32, (1, 0, 0, 0), (0, 0, 0, 0), b), b[-1])
        step.cache_clear()
        part2 *= tmp[0][-1]

print(f'Part 2: {part2}')
print(f'time: {pfc() - start}')
