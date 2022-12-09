from time import perf_counter as pfc
start = pfc()

forest = []
with open('input/8.txt') as f:
      forest = [[int(v) for v in s.strip()]for s in f.readlines()]

invisible = [[0]*len(forest[0]) for z in range(len(forest))]
scenic = [[1]*len(forest[0]) for z in range(len(forest))]
rows = len(forest)
cols = len(forest[0])

max_value = [-1] * rows
for x in range(cols):
    for i, v in enumerate(max_value):
        if forest[i][x] > v:
            max_value[i] = forest[i][x]
            invisible[i][x] = 1

        view = 0
        for view in range(x-1, -1, -1):
            if forest[i][x] <= forest[i][view]:
                break
        scenic[i][x] *= x - view

max_value = [-1] * rows
for x in range(cols-1, -1, -1):
    for i, v in enumerate(max_value):
        if forest[i][x] > v:
            max_value[i] = forest[i][x]
            invisible[i][x] = 1
        view = cols - 1
        for view in range(x+1, cols, 1):
            if forest[i][x] <= forest[i][view]:
                break
        scenic[i][x] *= view - x

max_value = [-1] * cols
for y in range(rows):
    for i, v in enumerate(max_value):
        if forest[y][i] > v:
            max_value[i] = forest[y][i]
            invisible[y][i] = 1

        view = 0
        for view in range(y-1, -1, -1):
            if forest[y][i] <= forest[view][i]:
                break
        scenic[y][i] *= y-view

max_value = [-1] * cols
for y in range(rows-1, -1, -1):
    for i, v in enumerate(max_value):
        if forest[y][i] > v:
            max_value[i] = forest[y][i]
            invisible[y][i] = 1
        view = rows - 1
        for view in range(y + 1, rows, 1):
            if forest[y][i] <= forest[view][i]:
                break
        scenic[y][i] *= view - y

print(f'part 1: {sum([sum(f) for f in invisible])}')
print(f'part 2: {max([max(s) for s in scenic])}')
print(f'time: {pfc() - start}')
