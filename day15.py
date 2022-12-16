from time import perf_counter as pfc

start = pfc()
part1_line = 2000000
x_range = range(0, 4000000)
y_range = range(0, 4000000)
sensors = []
part1 = -1
part2 = -1
part1_beacon = set()

with open('input/15.txt') as f:
    for line in f.readlines():
        z = line.strip().replace('Sensor at x=', '').replace(': closest beacon is at x=', ',').replace(' y=', '').split(',')
        xS, yS, xB, yB = map(int, z)
        manheten = abs(xS-xB)+abs(yS-yB)
        sensors.append([(xS, yS), (xB, yB), manheten, yS-manheten, yS+manheten])
        if yB == part1_line:
            part1_beacon.add(xB)

finding = False

for s in sensors:
    for s2 in sensors:
        m = abs(s[0][0]-s2[0][0])+abs(s[0][1]-s2[0][1])
        if m-s[2]-s2[2] == 2:
            m = s[2] + 1
            st = s[0][0] - m
            if st < x_range.start:
                st = x_range.start
            end = s[0][0] + m

            if end > x_range.stop:
                end = x_range.stop
            for x in range(st, end + 1):
                t = m - abs(s[0][0] - x)
                y1 = t + s[0][1]
                y2 = -t + s[0][1]
                finding1 = True
                finding2 = True
                for s1 in sensors:
                    if y_range.start <= y1 <= y_range.stop:
                        if (abs(s1[0][0] - x) + abs(s1[0][1] - y1)) <= s1[2]:
                            finding1 = False
                    if y1 != y2 and y_range.start <= y2 <= y_range.stop:
                        if (abs(s1[0][0] - x) + abs(s1[0][1] - y2)) <= s1[2]:
                            finding2 = False
                if finding1:
                    part2 = x * 4000000 + y1
                    break
                elif finding2:
                    part2 = x * 4000000 + y2
                    break
            break
print(f'Part 2: {part2}')
print(f'time: {pfc() - start}')
part2 = -1

def cmp(a):
    return a.start

def get_ranges(line, sen, ran):
    for s in sen:
        if s[3] <= line <= s[4]:
            t = s[2] - abs(s[0][1] - line)
            ran.append(range(s[0][0] - t, s[0][0] + t + 1))


def merge_ranges(ran):
    i = 1
    while i < len(ran):
        r = ran[i - 1]
        tmp_r = ran[i]
        if r.start <= tmp_r.start <= r.stop:
            if tmp_r.stop > r.stop:
                ran[i - 1] = range(r.start, tmp_r.stop)
            ran.pop(i)
        elif r.start <= tmp_r.stop <= r.stop:
            ran[i - 1] = range(tmp_r.start, r.stop)
            ran.pop(i)
        elif tmp_r.start <= r.start <= tmp_r.stop and tmp_r.start <= r.stop <= tmp_r.stop:
            ran[i - 1] = tmp_r
            ran.pop(i)
        else:
            i += 1


def find(start, stop):
    global part1
    global part2
    for y in range(start, stop):
        ranges = []
        get_ranges(y, sensors, ranges)
        ranges.sort(key=cmp)
        merge_ranges(ranges)

        if len(ranges) > 1:
            part2 = ranges[0].stop * 4000000 + y

        if y == part1_line:
            part1 = sum([r.stop - r.start for r in ranges]) - len(part1_beacon)
        if part1 > 0 and part2 > 0:
            break

find(0, y_range.stop)

#assert part1 == 5878678, f'{part1} Part1 wrong'
#assert part2 == 11796491041245, f'{part2} Part2 wrong'

print(f'part 1: {part1}')
print(f'part 2: {part2}')
print(f'time: {pfc() - start}')
