from time import perf_counter as pfc

start = pfc()
with open('input/22.txt') as f:
    maps, path = f.read().split('\n\n')
    maps = maps.split('\n')
    for i in range(len(maps)):
        maps[i] = maps[i].ljust(150, ' ')
path = list(map(int, path.replace('R', ' 1 ').replace('L', ' -1 ').split(' ')+['1']))


def part(part):
    part -= 1
    position = [maps[0].index('.'), 0]
    direction = 0
    z = (((lambda x, y: (0, [50, y]), lambda x, y: (0, [50, y]), lambda x, y: (0, [0, y]), lambda x, y: (0, [0, y])),
          (lambda x, y: (2, [99, 149 - y]), lambda x, y: (3, [50 + y, 49]),
           lambda x, y: (2, [149, 149 - y]), lambda x, y: (3, [y - 100, 149]))),
         ((lambda x, y: (1, [x, 100]), lambda x, y: (1, [x, 0]), lambda x, y: (1, [x, 0])),
          (lambda x, y: (1, [100 + x, 0]), lambda x, y: (2, [49, 100 + x]), lambda x, y: (2, [99, x - 50]))),
         ((lambda x, y: (2, [149, y]), lambda x, y: (2, [99, y]), lambda x, y: (2, [99, y]), lambda x, y: (2, [49, y])),
          (lambda x, y: (0, [0, 149 - y]), lambda x, y: (1, [y - 50, 100]), lambda x, y: (0, [50, 149 - y]),
           lambda x, y: (1, [y - 100, 0]))),
         ((lambda x, y: (3, [x, 199]), lambda x, y: (3, [x, 149]), lambda x, y: (3, [x, 49])),
          (lambda x, y: (0, [50, 50 + x]), lambda x, y: (0, [0, 100 + x]), lambda x, y: (3, [x - 100, 199]))))
    ww = (
        lambda x, y, d, pa: z[d][pa][y // 50](x, y) if len(maps[y]) <= x + 1 or maps[y][x + 1] == ' ' else (
            d, [x + 1, y]),
        lambda x, y, d, pa: z[d][pa][x // 50](x, y) if len(maps) <= y + 1 or maps[y + 1][x] == ' ' else (d, [x, y + 1]),
        lambda x, y, d, pa: z[d][pa][y // 50](x, y) if x - 1 < 0 or maps[y][x - 1] == ' ' else (d, [x - 1, y]),
        lambda x, y, d, pa: z[d][pa][x // 50](x, y) if y - 1 < 0 or maps[y - 1][x] == ' ' else (d, [x, y - 1]))

    for p in range(0, len(path), 2):
        sm = path[p]
        while sm > 0:
            new_dir, new_pos = ww[direction](position[0], position[1], direction, part)
            direction, position, sm = (new_dir, new_pos, sm-1) if maps[new_pos[1]][new_pos[0]] == '.' else (direction, position, 0)

        direction += path[p + 1]
        direction = 0 if direction > 3 else 3 if direction < 0 else direction

    return (position[1] + 1) * 1000 + (position[0] + 1) * 4 + direction


Part1 = part(1)
Part2 = part(2)
print(f'Part 1:{Part1}')
print(f'Part 2:{Part2}')
print(f'time: {pfc() - start}')
