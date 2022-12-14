from time import perf_counter as pfc

start = pfc()
start_point = (500, 0)
max_y = 0
sand_and_walls = set()

with open('input/14.txt') as f:
    for line in f.readlines():
        old_x = None
        old_y = None
        for point in line.split('->'):
            new_x, new_y = (map(int, point.strip(' ').split(',')))
            if old_x is not None:
                if old_x == new_x:
                    for y in range(min(old_y, new_y), max(old_y, new_y)+1):
                        sand_and_walls.add((old_x, y))
                else:
                    for x in range(min(old_x, new_x), max(old_x, new_x)+1):
                        sand_and_walls.add((x, old_y))
            old_x = new_x
            old_y = new_y
            if new_y > max_y:
                max_y = new_y

floor_y = max_y + 2
count_walls = len(sand_and_walls)
grain = None
part1 = 0
route = [start_point]
while grain != start_point:
    moved = True
    grain = route[-1]
    while moved:
        moved = False
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            tmp = (grain[0]+dx, grain[1]+dy)
            t = tmp[0]*1000 + tmp[1]
            if tmp[1] == floor_y or tmp in sand_and_walls:
                continue
            else:
                moved = True
                grain = tmp
                route.append(grain)
                break
    if part1 == 0 and grain[1] >= max_y:
        part1 = len(sand_and_walls) - count_walls
    route.pop()
    sand_and_walls.add(grain)

print(f'Part 1: {part1}')
print(f'Part 2: {len(sand_and_walls)- count_walls}')
print(f'time: {pfc() - start}')
