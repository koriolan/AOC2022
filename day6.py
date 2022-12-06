with open('input/6.txt') as f:
    key = f.read(4)
    for l in f.read():
        if len(set(key[-4:])) == 4:
            break
        else:
            key += l
print(f'part 1: {len(key)}')

with open('input/6.txt') as f:
        key = f.read(14)
        for l in f.read():
            if len(set(key[-14:])) == 14:
                break
            else:
                key += l


print(f'part 2: {len(key)}')