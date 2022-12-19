from time import perf_counter as pfc

start = pfc()
width = 7
rocks = [tuple((0b00011110,)), (0b00001000, 0b00011100, 0b00001000), (0b00011100, 0b00000100, 0b00000100),
         (0b00010000, 0b00010000, 0b00010000, 0b00010000), (0b00011000, 0b00011000)]
rocks_id = 0
dir_id = 0

with open('input/17.txt') as f:
    directions = f.readline().strip()

tower = [0b11111111]

stoped = 0
tmp = rocks[rocks_id]
pos = 3
while stoped < 4:

    if directions[dir_id] == '<':
        if all([(r << 1 & 0b10000000) != 0b10000000 for r in tmp]):
            t = pos
            left = True
            for r in tmp:
                if t >= len(tower):
                    break
                if (r ^ tower[t]) != (r | tower[t]):
                    left = False
                    break
                t += 1
            if left:
                tmp = tuple(tmp[r] << 1 for r in range(len(tmp)))
    else:
        if all([(r & 1) == 0 for r in tmp]):
            t = pos
            right = True
            for r in tmp:
                if t >= len(tower):
                    break
                if (r ^ tower[t]) != (r | tower[t]):
                    right = False
                    break
                t += 1
            if right:
                tmp = tuple(tmp[r] >> 1 for r in range(len(tmp)))
    dir_id += 1
    if dir_id >= len(directions):
        dir_id = 0

    t = pos
    down = True
    for r in tmp:
        if t >= len(tower):
            break
        if (r ^ tower[t]) != (r | tower[t]):
            down = False
            break
        t += 1

    if down:
        pos -= 1
    else:
        pos += 1
        for r in tmp:
            if pos < len(tower):
                tower[pos] = tower[pos] ^ r
            else:
                tower.append(r)
            pos += 1
        rocks_id += 1
        pos = len(tower) + 2
        if rocks_id >= len(rocks):
            rocks_id = 0
        tmp = rocks[rocks_id]

        stoped += 1
        # for k in range(-1, -len(tower)-1, -1):
        #     print(f'{tower[k]:08b}')
        # print('===================')
for k in range(-1, -len(tower)-1, -1):
        print(f'{tower[k]:08b}')
print(len(tower))
