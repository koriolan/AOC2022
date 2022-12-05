with open('input/4.txt') as f:
    s = [[{*range(k[0], k[1] + 1)} for k in [[int(k) for k in i.split('-')] for i in l[:-1].split(',')]] for l in f.readlines()]
    part1 = sum([1 if a[0] <= a[1] or a[0] <= a[1] else 0 for a in s])
    part2 = sum([0 if a[0].isdisjoint(a[1]) else 1 for a in s])
    print(f'part 1: {part1}')
    print(f'part 2: {part2}')
