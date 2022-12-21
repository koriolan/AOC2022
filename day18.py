from time import perf_counter as pfc

start = pfc()
n = 20
lava = []
lava1 = [[[0 for x in range(n)] for y in range(n)] for z in range(n)]
with open('input/18.txt') as f:
    for l in f.readlines():
        x, y, z = map(int, l.strip().split(','))
        lava1[z][y][x] = 1
        lava.append((x, y, z))


def surf(l):
    edge = set()
    per = set()

    for x, y, z in l:
        cube = [((x - 1, y, z), (x, y, z), (x, y-1, z), (x-1, y-1, z)),
                ((x - 1, y, z - 1), (x, y, z-1), (x, y - 1, z-1), (x - 1, y - 1, z-1)),
                ((x - 1, y, z - 1), (x - 1, y, z), (x - 1, y - 1, z), (x - 1, y - 1, z)),
                ((x - 1, y, z), (x, y, z), (x, y, z - 1), (x - 1, y, z - 1)),
                ((x - 1, y - 1, z), (x, y - 1, z), (x, y - 1, z - 1), (x - 1, y - 1, z - 1)),
                ((x, y, z-1), (x, y, z), (x, y - 1, z), (x, y - 1, z))]
        for tmp in cube:
            if tmp in edge:
                per.add(tmp)
            else:
                edge.add(tmp)
    return edge - per


def BFS(s):
    global lava1
    cur = 3
    while len(s) > 0:
        x, y, z = s.pop()
        if z - 1 > 0:
            if lava1[z-1][y][x] == 1:
                cur = 2
            elif lava1[z-1][y][x] == 0:
                s.add((x, y, z-1))
        if z + 1 < n:
            if lava1[z + 1][y][x] == 1:
                cur = 2
            elif lava1[z + 1][y][x] == 0:
                s.add((x, y, z + 1))
        if x - 1 > 0:
            if lava1[z][y][x - 1] == 1:
                cur = 2
            elif lava1[z][y][x - 1] == 0:
                s.add((x - 1, y, z))
        if x + 1 < n:
            if lava1[z][y][x+1] == 1:
                cur = 2
            elif lava1[z][y][x+1] == 0:
                s.add((x+1, y, z))
        if y - 1 > 0:
            if lava1[z][y - 1][x] == 1:
                cur = 2
            elif lava1[z][y - 1][x] == 0:
                s.add((x, y - 1, z))
        if y + 1 < n:
            if lava1[z][y+1][x] == 1:
                cur = 2
            elif lava1[z][y+1][x] == 0:
                s.add((x, y+1, z))
        lava1[z][y][x] = cur


surface = surf(lava)

BFS({(0, 0, 0)})
inside = set()
for z in range(n):
    for y in range(n):
        for x in range(n):
            if lava1[z][y][x] == 0:
                inside.add((x, y, z))

outside = surface-surf(inside)

print(f'part 1: {len(surface)}')
print(f'part 2: {len(outside)}')
print(f'time: {pfc() - start}')
