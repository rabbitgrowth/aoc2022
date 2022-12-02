with open('input.txt') as f:
    xs = [list(map(int, par.split())) for par in f.read().split('\n\n')]

print(max(map(sum, xs)))
print(sum(sorted(map(sum, xs), reverse=True)[:3]))
