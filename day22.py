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


def part(part1=True):
    position = [maps[0].index('.'), 0]
    direction = 0

    for p in range(0, len(path), 2):
        sm = int(path[p])
        while sm > 0:
            if direction == 0:  # right
                if len(maps[position[1]]) <= position[0] + 1 or maps[position[1]][position[0] + 1] == ' ':
                    if part1:
                        sm = findRight(sm, position)
                    else:
                        new_pos = []
                        if 0 <= position[1] < 50:
                            direction = 2
                            new_pos = [99, 100 + position[1]]
                        elif 50 <= position[1] < 100:
                            direction = 3
                            new_pos = [100 + position[1] - 50, 49]
                        elif 100 <= position[1] < 150:
                            direction = 2
                            new_pos = [149, position[1] - 100]
                        elif 150 <= position[1] < 200:
                            direction = 3
                            new_pos = [50 + position[1] - 150, 149]
                        else:
                            assert 1 != 1, f'{position}, Right'

                        if maps[new_pos[1]][new_pos[0]] == '#':
                            sm = 0
                        else:
                            position = new_pos
                            sm -= 1
                elif maps[position[1]][position[0] + 1] == '.':
                    position[0] += 1
                    sm -= 1
                else:
                    sm = 0

            elif direction == 1:  # Down
                if len(maps) <= position[1] + 1 or len(maps[position[1] + 1]) <= position[0] or maps[position[1] + 1][position[0]] == ' ':
                    if part1:
                        sm = findDown(sm, position)
                    else:
                        new_pos = []
                        if 0 <= position[0] < 50:
                            direction = 1
                            new_pos = [100+position[0], 0]
                        elif 50 <= position[0] < 100:
                            direction = 2
                            new_pos = [49, 150 + position[0] - 50]
                        elif 100 <= position[0] < 150:
                            direction = 2
                            new_pos = [99, 50 + position[0] - 100]
                        else:
                            assert 1 != 1, f'{position}, Down'

                        if maps[new_pos[1]][new_pos[0]] == '#':
                            sm = 0
                        else:
                            position = new_pos
                            sm -= 1

                elif maps[position[1] + 1][position[0]] == '.':
                    position[1] += 1
                    sm -= 1
                else:
                    sm = 0

            elif direction == 2:  # LEFT
                if position[0] - 1 < 0 or maps[position[1]][position[0] - 1] == ' ':
                    if part1:
                        sm = findLeft(sm, position)
                    else:
                        new_pos = []
                        if 0 <= position[1] < 50:
                            direction = 0
                            new_pos = [0, 100 + position[1]]
                        elif 50 <= position[1] < 100:
                            direction = 1
                            new_pos = [position[1] - 50, 100]
                        elif 100 <= position[1] < 150:
                            direction = 0
                            new_pos = [50, position[1] - 100]
                        elif 150 <= position[1] < 200:
                            direction = 1
                            new_pos = [50 + position[1] - 150, 0]
                        else:
                            assert 1 != 1, f'{position}, Left'
                        if maps[new_pos[1]][new_pos[0]] == '#':
                            sm = 0
                        else:
                            position = new_pos
                            sm -= 1
                elif maps[position[1]][position[0] - 1] == '.':
                    position[0] -= 1
                    sm -= 1
                else:
                    sm = 0

            else:  # UP
                if position[1] - 1 < 0 or len(maps[position[1] - 1]) <= position[0] or maps[position[1] - 1][position[0]] == ' ':
                    if part1:
                        sm = findUp(sm, position)
                    else:
                        new_pos = []
                        if 0 <= position[0] < 50:
                            direction = 0
                            new_pos = [50, 50 + position[0]]
                        elif 50 <= position[0] < 100:
                            direction = 0
                            new_pos = [0, 150 + position[0] - 50]
                        elif 100 <= position[0] < 150:
                            direction = 3
                            new_pos = [position[0]-100, 199]
                        else:
                            assert 1 != 1, f'{position}, Up'
                        if maps[new_pos[1]][new_pos[0]] == '#':
                            sm = 0
                        else:
                            position = new_pos
                            sm -= 1
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


# Part1 = part()
Part2 = part(False)
# print(f'Part 1:{Part1}')
print(f'Part 2:{Part2}')
print(f'time: {pfc() - start}')
