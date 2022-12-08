from time import perf_counter as pfc
start = pfc()

score = {'A X\n': [4, 3], 'A Y\n': [8, 4], 'A Z\n': [3, 8], 'B X\n': [1, 1], 'B Y\n': [5, 5], 'B Z\n': [9, 9], 'C X\n': [7, 2], 'C Y\n': [2, 6], 'C Z\n': [6, 7]}
print(f'part 1:{sum(map(lambda x: score[x][0], open("input/2.txt").readlines()))}')
print(f'part 2:{sum(map(lambda x: score[x][1], open("input/2.txt").readlines()))}')
print(f'time: {pfc() - start}')
