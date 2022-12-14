import itertools

def irange(a, b):
    return range(a, b + 1)

with open('input.txt') as f:
    rock = set()
    for line in map(str.rstrip, f):
        for points in itertools.pairwise(line.split(' -> ')):
            (x1, y1), (x2, y2) = (map(int, point.split(',')) for point in points)
            rock.update((x, y)
                        for x in irange(*sorted((x1, x2)))
                        for y in irange(*sorted((y1, y2))))

START = (500, 0)
MOVES = [(0, 1), (-1, 1), (1, 1)]
FLOOR = max(y for x, y in rock) + 2

sand = set()
seen_floor = False

while START not in sand:
    x, y = START
    while True:
        if y + 1 == FLOOR:
            if not seen_floor:
                print(len(sand))
                seen_floor = True
            sand.add((x, y))
            break
        for dx, dy in MOVES:
            new_x = x + dx
            new_y = y + dy
            if all((new_x, new_y) not in points for points in (rock, sand)):
                x = new_x
                y = new_y
                break
        else:
            sand.add((x, y))
            break

print(len(sand))
