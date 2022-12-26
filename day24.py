from time import perf_counter as pfc

start_pfc = pfc()
width = 0
height = 0
d = {'<': (-1, 0), '^': (0, -1), 'v': (0, 1), '>': (1, 0)}
blizzards = {}
with open('input/24.txt') as f:
    for y, s in enumerate(f.readlines()):
        for x, c in enumerate(s):
            if c in d:
                if (x, y) in blizzards:
                    blizzards[(x, y)].add(d[c])
                else:
                    blizzards[(x, y)] = {d[c]}
        height = y
        width = len(s) - 2
height -= 1


def find(st, end, blizzard):
    maybe = {st}
    stp = 0
    run = True
    while run:
        add = set()
        remove = set()
        stp += 1
        tmp = {}
        for b, directions in blizzard.items():
            for direction in directions:
                x = b[0] + direction[0]
                y = b[1] + direction[1]
                x = width if x == 0 else 1 if x > width else x
                y = height if y == 0 else 1 if y > height else y
                if (x, y) in tmp:
                    tmp[(x, y)].add(direction)
                else:
                    tmp[(x, y)] = {direction}
        blizzard = tmp

        for xm, ym in maybe:
            if end in ((xm, ym+1), (xm, ym-1)):
                run = False
                break
            if (xm, ym) in blizzard:
                remove.add((xm, ym))
            if xm + 1 <= width and 0 < ym <= height and (xm + 1, ym) not in blizzard:
                add.add((xm + 1, ym))
            if xm - 1 > 0 and 0 < ym <= height and (xm - 1, ym) not in blizzard:
                add.add((xm - 1, ym))
            if ym + 1 <= height and 0 < xm <= width and (xm, ym + 1) not in blizzard:
                add.add((xm, ym + 1))
            if ym - 1 > 0 and 0 < xm <= width and (xm, ym - 1) not in blizzard:
                add.add((xm, ym - 1))

        maybe.difference_update(remove)
        maybe.update(add)
    return stp, blizzard


part1, blizzards = find((1, 0), (width, height+1), blizzards)
st, blizzards = find((width, height+1), (1, 0), blizzards)
st2, blizzards = find((1, 0), (width, height+1), blizzards)
part2 = part1 + st + st2

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'time: {pfc() - start_pfc}')
