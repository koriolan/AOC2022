from time import perf_counter as pfc
start = pfc()


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

    def turn(self, calm, part1=True):
        result = []
        for i in self.items:
            result.append(self.testing(i, calm, part1))
            self.tested += 1
        self.items = []
        return result

    def testing(self, item, calm,  part1=True):
        tmp = self.operation[0](item, self.operation[1] if self.operation[1] else item)
        if part1:
            tmp //= calm
        else:
            tmp %= calm
        return self.true if tmp % self.test == 0 else self.false, tmp

    def add(self, item):
        self.items.append(item)


monkeys = []


def load_monkey():
    global monkeys
    monkeys = []
    with open('input/11.txt') as f:
        for monkey in f.read().split('\n\n'):
            m = [i.strip(' ').split(' ') for i in monkey.split('\n')]
            monkeys.append(Monkey(m[1][2:], m[2][-2:], m[3][-1], m[4][-1], m[5][-1]))


load_monkey()
for r in range(20):
    for m in monkeys:
        res = m.turn(3)
        for n, i in res:
            monkeys[n].add(i)

tested = [m.tested for m in monkeys]
tested.sort()
print(f'part 1: {tested[-1]*tested[-2]}')

load_monkey()
calm = 1
for m in monkeys:
    calm *= m.test
for r in range(10000):
    for m in monkeys:
        res = m.turn(calm, False)
        for n, i in res:
            monkeys[n].add(i)

tested = [m.tested for m in monkeys]
tested.sort()
print(f'part 2: {tested[-1]*tested[-2]}')
print(f'time: {pfc() - start}')
