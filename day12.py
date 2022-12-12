import sys
from time import perf_counter as pfc

start = pfc()

maps = []
with open('input/12.txt') as f:
    maps = [[ord(j) for j in i.strip()] for i in f.readlines()]

h = len(maps)
w = len(maps[0])
start_position = (0, 0)
end_position = (0, 0)

le = [[(sys.maxsize, True)]*w for i in range(h)]

maybe_start = set()

for idx, s in enumerate(maps):
    for idy, o in enumerate(s):
        if o == ord('S'):
            start_position = (idx, idy)
            maps[idx][idy] = ord('a')
            maybe_start.add((idx, idy))
        elif o == ord('E'):
            end_position = (idx, idy)
            maps[idx][idy] = ord('z')
        elif o == ord('a'):
            maybe_start.add((idx, idy))


le[end_position[0]][end_position[1]] = (0, True)
visited = 0
not_view = {(end_position[0], end_position[1]): 0}

while len(not_view) > 0:
    v = sys.maxsize
    a1 = 0
    b1 = 0
    for k in not_view:
        if not_view[k] < v:
            v = not_view[k]
            a1 = k[0]
            b1 = k[1]

    for a2, b2 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        a = a1 + a2
        b = b1 + b2
        if 0 <= a < h and 0 <= b < w:
            if le[a][b][1] and le[a][b][0] > (v + 1) and maps[a1][b1] <= maps[a][b]+1:
                not_view[(a, b)] = v+1
                le[a][b] = (v + 1, True)
    le[a1][b1] = (le[a1][b1][0], False)
    not_view.pop((a1, b1))
    visited += 1

part2 = sys.maxsize
for a, b in maybe_start:
    if part2 > le[a][b][0]:
        part2 = le[a][b][0]

print(f'part 1: {le[start_position[0]][start_position[1]][0]}')
print(f'part 2: {part2}')
print(f'time: {pfc() - start}')
