lava = []
with open('18.txt') as f:
    for l in f.readlines():
        x, y, z = map(int, l.strip().split(','))
        lava.append((x, y, z))

edge = set()
per = set()
for x, y, z in lava:
    cube = [((x - 1, y, z), (x, y, z), (x, y-1, z), (x-1, y-1, z)),
            ((x - 1, y, z - 1), (x, y, z-1), (x, y - 1, z-1), (x - 1, y - 1, z-1)),
            ((x - 1, y, z - 1), (x - 1, y, z), (x - 1, y - 1, z), (x - 1, y - 1, z)),
            ((x - 1, y, z), (x, y, z), (x, y, z - 1), (x - 1, y, z - 1)),
            ((x - 1, y - 1, z), (x, y - 1, z), (x, y - 1, z - 1), (x - 1, y - 1, z - 1)),
            ((x, y, z-1), (x, y, z), (x, y - 1, z), (x, y - 1, z))]
    for tmp in cube:
        if tmp in edge:
            per.add(tmp)
        else:
            edge.add(tmp)

i = 0
for x, y, z in lava:
    cube = [((x - 1, y, z), (x, y, z), (x, y - 1, z), (x - 1, y - 1, z)),
            ((x - 1, y, z - 1), (x, y, z - 1), (x, y - 1, z - 1), (x - 1, y - 1, z - 1)),
            ((x - 1, y, z - 1), (x - 1, y, z), (x - 1, y - 1, z), (x - 1, y - 1, z)),
            ((x - 1, y, z), (x, y, z), (x, y, z - 1), (x - 1, y, z - 1)),
            ((x - 1, y - 1, z), (x, y - 1, z), (x, y - 1, z - 1), (x - 1, y - 1, z - 1)),
            ((x, y, z - 1), (x, y, z), (x, y - 1, z), (x, y - 1, z))]

    f = False
    if not any(tmp in per for tmp in cube):
        print(x,y,z)
print(len(edge) - len(per))
print(len(edge)-len(per)-i*6)