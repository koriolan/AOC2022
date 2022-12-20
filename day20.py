from time import perf_counter as pfc

start = pfc()
with open('input/20.txt') as f:
    encrypted = list(map(int, [line.strip() for line in f.readlines()]))


def decrypt(repeat, enc):
    cnt = len(encrypted)
    p = list(range(cnt))
    for i in range(repeat):
        for idx, v in enumerate(enc):
            if v == 0:
                continue
            old_idx = p.index(idx)
            new_idx = old_idx + v
            if new_idx >= cnt:
                new_idx = new_idx % (cnt-1)
            elif new_idx < 0:
                new_idx = cnt-(cnt - (new_idx % (cnt-1)))
            p.pop(old_idx)
            p.insert(new_idx, idx)
    zero_idx = p.index(enc.index(0))
    return sum(enc[p[(zero_idx+gps) % cnt]] for gps in [1000, 2000, 3000])


part1 = decrypt(1, encrypted)
part2 = decrypt(10, [i*811589153 for i in encrypted])

print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
print(f'time: {pfc() - start}')
