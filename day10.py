from time import perf_counter as pfc
start = pfc()

x = 1
cycle = 0
crt = 0
sprite_position = range(3)
part1 = 0
part2 = ''


def cycleInc():
    global cycle, part1, part2, crt
    cycle += 1

    if crt in sprite_position:
        part2 += '#'
    else:
        part2 += ' '

    if (cycle+20) % 40 == 0:
        part1 += x * cycle
    elif cycle % 40 == 0:
        crt = -1
        part2 += '\n'
    crt += 1


with open('input/10.txt') as f:
    for line in f.readlines():
        a = line.strip().split(' ')
        cycleInc()
        if a[0] == 'addx':
            cycleInc()
            x += int(a[1])
            sprite_position = range(x-1, x+2)


print(f'part 1: {part1}')
print('part 2:')
print(part2)
print(f'time: {pfc() - start}')
