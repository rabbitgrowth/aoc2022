import math

class Monkey:
    def __init__(self, items, operation, divisor, targets):
        self.items     = items
        self.operation = operation
        self.divisor   = divisor
        self.targets   = targets
        self.inspections = 0

for rounds, divide in ((20, True), (10000, False)):
    with open('input.txt') as f:
        monkeys = []
        for par in f.read().split('\n\n'):
            a, b, c, d, e = par.splitlines()[1:]
            items     = list(map(int, a.split(': ')[1].split(', ')))
            operation = b.split()[-2:]
            divisor   = int(c.split()[-1])
            targets   = [int(line.split()[-1]) for line in (d, e)]
            monkeys.append(Monkey(items, operation, divisor, targets))

    product = math.prod(monkey.divisor for monkey in monkeys)

    for _ in range(rounds):
        for i, monkey in enumerate(monkeys):
            monkey.inspections += len(monkey.items)
            for item in monkey.items:
                match monkey.operation:
                    case ('*', 'old'):
                        item **= 2
                    case ('*', x):
                        item *= int(x)
                    case ('+', x):
                        item += int(x)
                if divide:
                    item //= 3
                else:
                    item %= product
                target = monkeys[monkey.targets[bool(item % monkey.divisor)]]
                target.items.append(item)
            monkey.items.clear()

    print(math.prod(sorted(monkey.inspections for monkey in monkeys)[-2:]))
