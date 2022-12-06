with open('input/6.txt') as f:
    key = f.read(4)
    i = 4
    for l in f.read():
        if len(set(key)) == 4:
            break
        else:
            key = key[1:] + l
            i += 1

with open('input/6.txt') as f:
        key = f.read(14)
        j = 14
        for l in f.read():
            if len(set(key)) == 14:
                break
            else:
                key = key[1:] + l
                j += 1

print(f'part 1: {i}')
print(f'part 2: {j}')