with open('input.txt') as f:
    numbers = [list(map(int, par.split())) for par in f.read().split('\n\n')]

print(max(map(sum, numbers)))
print(sum(sorted(map(sum, numbers), reverse=True)[:3]))
