import functools
from time import perf_counter as pfc

start = pfc()


blueprints = set()
i = 1
with open('input/19.txt') as f:
    for line in f.readlines():
        costs = line.strip().replace('.', '').split(' ')
        blueprints.add((int(costs[6]), int(costs[12]), (int(costs[18]), int(costs[21])), (int(costs[27]), int(costs[30])),
                        (max([int(costs[6]), int(costs[12]), int(costs[18]), int(costs[27])])+1, int(costs[21]), int(costs[30])), i))
        i += 1


@functools.cache
def step(cnt, robots, solid, blueprint):
    if cnt == 1:
        return solid[-1] + robots[-1]
    #if robots[0] >= blueprint[3][0] and robots[2] >= blueprint[3][1]:
    #    return solid[-1] + sum(range(cnt))+1
    maybe = [((0, 0, 0, 0), (0, 0, 0, 0))]
    if blueprint[3][0] <= solid[0] and blueprint[3][1] <= solid[2]:
        maybe = [((0, 0, 0, 1), (-blueprint[3][0], 0, -blueprint[3][1], 0))]
    elif blueprint[2][0] <= solid[0] and blueprint[2][1] <= solid[1] and blueprint[-2][0] >= robots[2]:
        maybe = [((0, 0, 1, 0), (-blueprint[2][0], -blueprint[2][1], 0, 0))]
    else:
        if blueprint[0] <= solid[0] and blueprint[-2][0] >= robots[0]:
            maybe.append(((1, 0, 0, 0), (-blueprint[0], 0, 0, 0)))
        if blueprint[1] <= solid[0] and blueprint[-2][1] >= robots[1]:
            maybe.append(((0, 1, 0, 0), (-blueprint[1], 0, 0, 0)))

    max_geodes = -1
    for r, s in maybe:
        t = step(cnt-1, tuple(i for i in map(sum, zip(robots, r))), tuple(i for i in map(sum, zip(solid, robots, s))), blueprint)
        if t > max_geodes:
            max_geodes = t
    return max_geodes


# part1 = 0
# for b in blueprints:
#     tmp = (step(24, (1, 0, 0, 0), (0, 0, 0, 0), b), b[-1])
#     step.cache_clear()
#     part1 += tmp[-1] * tmp[0]
#
# print(f'Part 1: {part1}')
# print(f'time: {pfc() - start}')
# assert part1 == 1981
# start = pfc()
part2 = 1

for b in blueprints:
    if b[-1] in [1, 2, 3]:
        z = step(32, (1, 0, 0, 0), (0, 0, 0, 0), b)
        part2 *= z
        print(z)
        step.cache_clear()


print(f'Part 2: {part2}')
print(f'time: {pfc() - start}')
assert part2 == 10962
