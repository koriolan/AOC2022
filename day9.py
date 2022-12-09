import math
from time import perf_counter as pfc
start = pfc()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'({self.x},{self.y})'

    def distance(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def save(self):
        return self.x, self.y


directions = {'R': Point(1, 0), 'L': Point(-1, 0), 'U': Point(0, 1), 'D': Point(0, -1)}


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def draw_line(p0, p1):
    x, y = p0.x, p0.y
    A = p1.y - p0.y
    B = p0.x - p1.x
    dx, dy = -sign(B), sign(A)
    ex = A * dx
    ey = B * dy

    if abs(ex) < abs(ey):
        x += dx
    else:
        y += dy
    return Point(x, y)


def move(head, tail, direction):
    distance = tail.distance(head)
    if distance == 4:
         tail += direction
    # elif distance == 5:
    #     p = head - tail
    #     if abs(p.x) == 1:
    #         tail.x = head.x
    #         tail.y = head.y + 1 if p.y < 0 else head.y - 1
    #     else:
    #         tail.y = head.y
    #         tail.x = head.x + 1 if p.x < 0 else head.x - 1
    elif distance in (0, 1, 2):
        pass
    else:
        # xba = tail.x-head.x
        # yba = tail.y-head.y
        # xa = head.x
        # ya = head.y
        # maybe = set()
        # for dx in range(-1, 2, 1):
        #     for dy in range(-1, 2, 1):
        #         p = head + Point(dx, dy)
        #         if p.x-xa/xba == p.y-ya/yba:
        #             maybe.add(p)
        # min_p = maybe.pop()
        # min_d = tail.distance(min_p)
        # for p in maybe:
        #     d = tail.distance(p)
        #     if min_d > d:
        #         min_d = d
        #         min_p = p
        # tail = min_p
        tail = draw_line(head, tail)
    return tail


def move_rope(rope):
    points = set()
    with open('input/9.txt') as f:
        for line in f.readlines():
            a = line.split()
            c = int(a[1])
            d = directions[a[0]]
            for i in range(c):
                rope[0] += d
                for j in range(len(rope)-1):
                    rope[j+1] = move(rope[j], rope[j+1], d)
                points.add(rope[-1].save())
    return points


rope1 = [Point(0, 0) for r in range(2)]
print(f'part 1: {len(move_rope(rope1))}')

rope2 = [Point(0, 0) for r in range(10)]
print(f'part 2: {len(move_rope(rope2))}')
print(f'time: {pfc() - start}')
