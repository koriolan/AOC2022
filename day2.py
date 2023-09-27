from time import perf_counter as pfc
start = pfc()

score = {b'A X\n': (4, 3), b'A Y\n': (8, 4), b'A Z\n': (3, 8), b'B X\n': (1, 1), b'B Y\n': (5, 5), b'B Z\n': (9, 9), b'C X\n': (7, 2), b'C Y\n': (2, 6), b'C Z\n': (6, 7)}
with open("input/2.txt",'rb') as f:
    lines = f.readlines()
    print(f'part 1:{sum(map(lambda x: score[x][0], lines))}')
    print(f'part 2:{sum(map(lambda x: score[x][1], lines))}')
print(f'time: {pfc() - start}')
