from time import perf_counter as pfc

start = pfc()
width = 7
rocks = [tuple((0b00011110,)), (0b00001000, 0b00011100, 0b00001000), (0b00011100, 0b00000100, 0b00000100),
         (0b00010000, 0b00010000, 0b00010000, 0b00010000), (0b00011000, 0b00011000)]


with open('input/17.txt') as f:
    directions = f.readline().strip()


def tetris(tow, cnt, r_id, d_id):
    povtor = {}
    stoped = 0
    pos = len(tow)+3
    tmp = rocks[r_id]

    while stoped < cnt:
        if directions[d_id] == '<':
            if all([(r & 0b01000000) == 0 for r in tmp]):
                t = pos
                left = True
                for r in tmp:
                    if t >= len(tow):
                        break
                    if ((r << 1) & tow[t]) != 0:
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
                    if t >= len(tow):
                        break
                    if ((r >> 1) & tow[t]) != 0:
                        right = False
                        break
                    t += 1
                if right:
                    tmp = tuple(tmp[r] >> 1 for r in range(len(tmp)))
        d_id += 1
        if d_id >= len(directions):
            d_id = 0

        t = pos - 1
        down = True
        for r in tmp:
            if t >= len(tow):
                break
            if (r & tow[t]) != 0:
                down = False
                break
            t += 1

        if down:
            pos -= 1
        else:
            for r in tmp:
                if pos < len(tow):
                    tow[pos] = tow[pos] ^ r
                else:
                    tow.append(r)
                pos += 1

            r_id += 1
            if r_id >= len(rocks):
                r_id = 0

            for i in range(1, len(tow)-1):
                if tow[i] | tow[i+1] == 127:
                    if (tow[i], tow[i+1], len(tow) - i-1, r_id, d_id) in povtor:
                        tmp = povtor[(tow[i], tow[i+1], len(tow) - i-1,  r_id, d_id)]
                        return tmp[0], tmp[1], len(tow)-1 - tmp[1], stoped - tmp[0], [tow[i], tow[i+1]], r_id, d_id
                    else:
                         povtor[(tow[i], tow[i+1], len(tow) - i-1, r_id, d_id)] = (stoped, len(tow)-1)

            pos = len(tow) + 3
            tmp = rocks[r_id]
            stoped += 1
    return (len(tow), )

def parts(n):
    h = 0
    res = tetris([0b11111111], n, 0, 0)

    if len(res) > 1:
        z = n-res[0]
        k = z//res[3]
        ost = z - k*res[3]
        h1 = tetris(res[4], ost, res[5], res[6])[0] - 2
        h = res[1] + k*res[2] + h1
    else:
        h = res[0]-1
    return h


print(f'part 1:{parts(2022)}')
print(f'part 2:{parts(1000000000000)}')
print(f'time: {pfc() - start}')


