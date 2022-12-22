from time import perf_counter as pfc

start = pfc()
with open('input/22.txt') as f:
    maps, path = f.read().split('\n\n')
    maps = maps.split('\n')

path = path.replace('R', ' R ').replace('L', ' L ').split(' ')


def findUp(sm, pos):
    for i in range(len(maps) - 1, -1, -1):
        if len(maps[i]) > pos[0]:
            if maps[i][pos[0]] == '.':
                pos[1] = i
                sm -= 1
                break
            elif maps[i][pos[0]] == '#':
                sm = 0
                break
    return sm


def findLeft(sm, pos):
    for i in range(len(maps[pos[1]]) - 1, -1, -1):
        if maps[pos[1]][i] == '.':
            pos[0] = i
            sm -= 1
            break
        elif maps[pos[1]][i] == '#':
            sm = 0
            break
    return sm


def findDown(sm, pos):
    for i in range(len(maps)):
        if maps[i][pos[0]] == '.':
            pos[1] = i
            sm -= 1
            break
        elif maps[i][pos[0]] == '#':
            sm = 0
            break
    return sm


def findRight(sm, pos):
    for i in range(len(maps[pos[1]])):
        if maps[pos[1]][i] == '.':
            pos[0] = i
            sm -= 1
            break
        elif maps[pos[1]][i] == '#':
            sm = 0
            break
    return sm


def part1():
    position = [maps[0].index('.'), 0]
    direction = 0

    for p in range(0, len(path), 2):
        sm = int(path[p])
        if direction == 0:  # right
            while sm > 0:
                if len(maps[position[1]]) <= position[0] + 1 or maps[position[1]][position[0] + 1] == ' ':
                    sm = findRight(sm, position)
                elif maps[position[1]][position[0] + 1] == '.':
                    position[0] += 1
                    sm -= 1
                else:
                    sm = 0

        elif direction == 1:  # Down
            while sm > 0:
                if len(maps) <= position[1] + 1 or len(maps[position[1] + 1]) <= position[0] or maps[position[1] + 1][position[0]] == ' ':
                    sm = findDown(sm, position)
                elif maps[position[1] + 1][position[0]] == '.':
                    position[1] += 1
                    sm -= 1
                else:
                    sm = 0

        elif direction == 2:  # LEFT
            while sm > 0:
                if position[0] - 1 < 0 or maps[position[1]][position[0] - 1] == ' ':
                    sm = findLeft(sm, position)
                elif maps[position[1]][position[0] - 1] == '.':
                    position[0] -= 1
                    sm -= 1
                else:
                    sm = 0

        else:  # UP
            while sm > 0:
                if position[1] - 1 < 0 or len(maps[position[1] - 1]) <= position[0] or maps[position[1] - 1][position[0]] == ' ':
                    sm = findUp(sm, position)
                elif maps[position[1] - 1][position[0]] == '.':
                    position[1] -= 1
                    sm -= 1
                else:
                    sm = 0

        if len(path) > p + 1:
            if path[p + 1] == 'R':
                direction += 1
                if direction > 3:
                    direction = 0
            else:
                direction -= 1
                if direction < 0:
                    direction = 3
    return (position[1] + 1) * 1000 + (position[0] + 1) * 4 + direction


def part2():
    pos = [0, 0]
    direction = 0
    a = 4
    cube = [[]]
    for i, k in enumerate(maps):
        cube[-1].append(k[a*2:])
        if i == 3:
            break
    for t in range(3):
        cube.append([])
        for i, k in enumerate(maps[a:]):
            cube[-1].append(k[a*t: a*t+a])
            if i == 3:
                break
    for t in range(2):
        cube.append([])
        for i, k in enumerate(maps[a+a:]):
            cube[-1].append(k[a*2+a * t: a*2+a * t + a])
            if i == 3:
                break
    for c in cube:
        print(c)

    for p in range(0, len(path), 2):
        sm = int(path[p])

        if len(path) > p + 1:
            if path[p + 1] == 'R':
                direction += 1
                if direction > 3:
                    direction = 0
            else:
                direction -= 1
                if direction < 0:
                    direction = 3


Part1 = part1()
Part2 = part2()
print(f'Part 1:{Part1}')
print(f'Part 2:{Part2}')
print(f'time: {pfc() - start}')
