# Semi-brute-force solution

import re

def manhattan(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

with open('input.txt') as f:
    sensors = []
    beacons = []
    for line in f:
        sx, sy, bx, by = map(int, re.findall('-?\d+', line))
        sensors.append((sx, sy))
        beacons.append((bx, by))

for y in range(4000000 + 1):
    ranges = []
    for (sx, sy), (bx, by) in zip(sensors, beacons):
        distance = manhattan((sx, sy), (bx, by))
        dy = abs(sy - y)
        if dy > distance:
            continue
        dx = distance - dy
        ranges.append((sx - dx, sx + dx))

    last = None
    for a, b in sorted(ranges):
        if last is not None:
            last_a, last_b = last
            if last_b + 1 >= a:
                a = last_a
                b = max(last_b, b)
            else:
                x = last_b + 1
                part2 = x * 4000000 + y
        last = (a, b)

    if y == 2000000:
        part1 = b - a + 1 - sum(by == y for bx, by in set(beacons))

print(part1)
print(part2)
