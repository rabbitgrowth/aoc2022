# I originally overthought part 1 and solved it in this weird way:

from collections import defaultdict

with open('input.txt') as f:
    points = {tuple(map(int, line.rstrip().split(','))) for line in f}

lines = defaultdict(list)

for x, y, z in points:
    lines[(None, y, z)].append(x)
    lines[(x, None, z)].append(y)
    lines[(x, y, None)].append(z)

surface_area = 0

for line in lines.values():
    last_n = None
    for n in sorted(line):
        if last_n is None or n - last_n > 1:
            surface_area += 2
        last_n = n

print(surface_area)
