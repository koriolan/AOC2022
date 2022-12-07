class Item:
    def __init__(self, name, size, parent, isdir=False):
        self.name = name
        self._size = size
        self.items = []
        self.parent = parent
        self.isDir = isdir

    def add(self, child):
        self.items.append(child)

    def get_size(self):
        if self._size is None:
            self._size = sum([i.get_size() for i in self.items])
        return self._size

    def getItemByName(self, name):
        if self.isDir:
            for i in self.items:
                if i.name == name:
                    return i
        return None


D = Item('/', None, None, True)
cur = D
with open('input/7.txt') as fi:
    for line in fi.readlines():
        tmp = line.strip('\n').split(' ')
        if tmp[0] == '$':
            if tmp[1] == 'cd':
                if tmp[2] == '/':
                    cur = D
                elif tmp[2] == '..':
                    cur = cur.parent
                else:
                    cur = cur.getItemByName(tmp[2])
            else:
                pass
        elif tmp[0] == 'dir':
            cur.add(Item(tmp[1], None, cur, True))
        else:
            cur.add(Item(tmp[1], int(tmp[0]), cur))


def sums(dirs):
    s = 0
    for i in dirs.items:
        if i.isDir:
            size = i.get_size()
            if size < 100000:
                s += size
            s += sums(i)
    return s


need = 30000000 - (70000000-D.get_size())
minDir = 70000000


def findMin(dirs, min_dir):
    for i in dirs.items:
        if i.isDir:
            size = i.get_size()
            if need < size < min_dir:
                min_dir = size
            tmp_min = findMin(i, min_dir)
            if need < tmp_min < min_dir:
                min_dir = tmp_min
    return min_dir


print(f'part 1: {sums(D)}')
print(f'part 2: {findMin(D, minDir)}')
