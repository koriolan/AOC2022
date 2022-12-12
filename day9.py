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


def move(head, tail):
    distance = tail.distance(head)
    p = head - tail
    if distance == 4:
         tail += Point(p.x//2, p.y//2)
    elif distance == 5:
        if abs(p.x) == 1:
            tail.x = head.x
            tail.y = head.y + 1 if p.y < 0 else head.y - 1
        else:
            tail.y = head.y
            tail.x = head.x + 1 if p.x < 0 else head.x - 1
    elif distance in (0, 1, 2):
        pass
    elif distance == 8:
        tail.x += (1 if p.x > 0 else -1)
        tail.y += (1 if p.y > 0 else -1)

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
                    rope[j+1] = move(rope[j], rope[j+1])
                points.add(rope[-1].save())

    return points


rope1 = [Point(0, 0) for r in range(2)]
print(f'part 1: {len(move_rope(rope1))}')

rope2 = [Point(0, 0) for r in range(10)]
print(f'part 2: {len(move_rope(rope2))}')
print(f'time: {pfc() - start}')
