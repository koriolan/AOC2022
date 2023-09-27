from time import perf_counter as pfc

start = pfc()

prior = lambda x: (x-38) % 58

with open('input/3.txt', 'rb') as f:
    lines = f.readlines()
    print(f'part 1: {sum([prior((set(l[:len(l)//2])&set(l[len(l)//2:])).pop()) for l in lines])}')
    print(f'part 2: {sum([prior(set.intersection(*[set(l[:-1]) for l in lines[i:i+3]]).pop()) for i in range(0,len(lines),3)])}')
print(f'time: {pfc() - start}')
