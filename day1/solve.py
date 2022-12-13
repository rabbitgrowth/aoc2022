with open('input.txt') as f:
    elves = sorted(sum(map(int, par.splitlines()))
                   for par in f.read().split('\n\n'))

print(elves[-1])
print(sum(elves[-3:]))
