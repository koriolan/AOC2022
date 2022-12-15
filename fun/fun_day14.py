import os
from time import perf_counter as pfc
from PIL import Image
start = pfc()
start_point = (500, 0)
max_y = 0
sand_and_walls = set()

with open('../input/14.txt') as f:
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
for x in range(500-floor_y, 500+floor_y+1):
    sand_and_walls.add((x, floor_y))

normol_x = 500-floor_y

count_walls = len(sand_and_walls)
grain = None
part1 = 0
route = [start_point]
pixel_size = 2


def drawPixel(img, xy , c):
    rx = (xy[0] - normol_x) * pixel_size
    ry = xy[1] * pixel_size
    for i in range(pixel_size):
        for j in range(pixel_size):
            img.putpixel((rx+i, ry+j), c)


if not os.path.isdir('fun_day14'):
    os.mkdir('fun_day14')
    os.mkdir('fun_day14/gif')
    os.mkdir('fun_day14/png')

n = 0
background = Image.new(mode="RGBA", size=((floor_y*2+1)*pixel_size, (floor_y+1)*pixel_size), color="black")
for x, y in sand_and_walls:
    drawPixel(background, (x, y), (255, 255, 255, 255))
background.save(f'fun_day14/png/{n}.png', 'PNG')
n += 1

fp_in = "fun_day14/png/*.png"
fp_out = "fun_day14/gif/"

while grain != start_point:
    moved = True
    grain = route[-1]
    while moved:
        moved = False
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            tmp = (grain[0]+dx, grain[1]+dy)
            if tmp not in sand_and_walls:
                moved = True
                grain = tmp
                route.append(grain)
                break
    if part1 == 0 and grain[1] >= max_y:
        part1 = len(sand_and_walls) - count_walls
    route.pop()
    sand_and_walls.add(grain)
    tmp_img = background
    drawPixel(tmp_img, grain, (244, 164, 96, 255))
    tmp_img.save(f'fun_day14/png/{n}.png', 'PNG')
    n += 1
    if len(sand_and_walls) % 1000 == 0:
        print(f'{n:5} time: {pfc() - start}')


print(f'Part 1: {part1}')
print(f'Part 2: {len(sand_and_walls)- count_walls}')
print(f'time: {pfc() - start}')
