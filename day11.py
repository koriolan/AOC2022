class Monkey:

    def __init__(self, items, operation, test, true, false):
        d = {'+': int.__add__, '*': int.__mul__}
        self.olded = {}
        self.items = [int(i.strip(',')) for i in items]
        if operation[1] == 'old':
            self.operation = [d[operation[0]], None]
        else:
            self.operation = [d[operation[0]], int(operation[1])]
        self.test = int(test)
        self.true = int(true)
        self.false = int(false)
        self.tested = 0

    def __str__(self):
        return f'{self.items} {self.operation} {self.test} {self.true} {self.false} {self.tested}'

    def __repr__(self):
        return str(self)

    def turn(self, part1=True):

        result = []
        for i in self.items:
            tmp = self.operation[0](i, self.operation[1] if self.operation[1] else i)
            if part1:
                tmp //= 3
            result.append((self.true if tmp % self.test == 0 else self.false, tmp))
            self.tested += 1
        self.items = []
        return result

    def add(self, item):
        self.items.append(item)


monkeys = []

with open('11.txt') as f:
    for monkey in f.read().split('\n\n'):
        m = [i.strip(' ').split(' ') for i in monkey.split('\n')]
        monkeys.append(Monkey(m[1][2:], m[2][-2:], m[3][-1], m[4][-1], m[5][-1]))
for r in range(20):
    for m in monkeys:
        res = m.turn()
        for n, i in res:
            monkeys[n].add(i)

tested = [m.tested for m in monkeys]
tested.sort()
print(f'part 1: {tested[-1]*tested[-2]}')


for r in range(10000):
    for m in monkeys:
        res = m.turn(False)
        for n, i in res:
            monkeys[n].add(i)
    for m in monkeys:
        print(m)

tested = [m.tested for m in monkeys]
tested.sort()
print(f'part 1: {tested[-1]*tested[-2]}')

