import sys
from time import perf_counter as pfc

start = pfc()
elves_old = set()
with open('input/23.txt') as f:
    for y, s in enumerate(f.readlines()):
        for x, p in enumerate(s):
            if p == '#':
                elves_old.add((x, y))

around = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (1, 1), (0, 1), (-1, 1))


def step(elves, direct):
    tmp = {}
    res = set()
    for e in elves:
        around_elves = False
        for a in around:
            if (e[0] + a[0], e[1] + a[1]) in elves:
                around_elves = True
                break
        if around_elves:
            find = False
            for check, d in direct:
                if all(((e[0]+c[0], e[1]+c[1]) not in elves for c in check)):
                    p = (e[0]+d[0], e[1]+d[1])
                    find = True
                    if p in tmp:
                        tmp[p].add(e)
                    else:
                        tmp[p] = {e}
                    break
            if not find:
                res.add(e)
        else:
            res.add(e)
    for p, e in tmp.items():
        if len(e) > 1:
            res.update(e)
        else:
            res.add(p)
    return res


directions = [[((-1, -1), (0, -1), (1, -1)), (0, -1)], [((-1, 1), (0, 1), (1, 1)), (0, 1)], [((-1, -1), (-1, 0), (-1, 1)), (-1, 0)], [((1, -1), (1, 0), (1, 1)), (1, 0)]]
new_elves = step(elves_old, directions)
part2 = 1
part1 = 0
while elves_old != new_elves:
    elves_old = new_elves
    directions.append(directions.pop(0))
    new_elves = step(elves_old, directions)
    part2 += 1
    if part2 == 10:
        min_x = sys.maxsize
        max_x = 0
        min_y = sys.maxsize
        max_y = 0
        for e in new_elves:
            if e[0] < min_x:
                min_x = e[0]
            if e[0] > max_x:
                max_x = e[0]

            if e[1] < min_y:
                min_y = e[1]
            if e[1] > max_y:
                max_y = e[1]
        part1 = (max_x-min_x+1)*(max_y-min_y+1)-len(new_elves)

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'time: {pfc() - start}')
