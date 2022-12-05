stock9000 = [[] for i in range(9)]
stock9001 = [[] for j in range(9)]
with open('input/5.txt') as f:
    start, moves = f.read().split('\n\n')
    for s in start.split('\n')[:-1]:
        for idx, k in enumerate(s):
            if k not in [' ', ']', '[']:
                stock9000[(idx - 1) // 4].insert(0, k)
                stock9001[(idx - 1) // 4].insert(0, k)

    for m in moves.split('\n'):
        a = m.split(' ')
        cnt, fr, to = int(a[1]), int(a[3])-1, int(a[5])-1
        for i in range(cnt):
            stock9000[to].append(stock9000[fr].pop())
        stock9001[to].extend(stock9001[fr][-cnt:])
        del stock9001[fr][-cnt:]
    print(f"part1 :{''.join([i[-1] if len(i) > 0 else '' for i in stock9000])}")
    print(f"part2 :{''.join([i[-1] if len(i) > 0 else '' for i in stock9001])}")
