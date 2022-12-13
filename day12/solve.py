import itertools
import string

with open('input.txt') as f:
    heightmap = []
    a = set()
    for y, line in enumerate(map(str.rstrip, f)):
        row = []
        for x, char in enumerate(line):
            if char == 'S':
                START = (x, y)
                row.append(0)
            elif char == 'E':
                END = (x, y)
                row.append(25)
            else:
                height = string.ascii_lowercase.index(char)
                row.append(height)
                if not height:
                    a.add((x, y))
        heightmap.append(row)

WIDTH  = len(heightmap[0])
HEIGHT = len(heightmap)

def solve(points):
    seen = set()
    for steps in itertools.count(1):
        new_points = set()
        for point in points:
            seen.add(point)
            x, y = point
            height = heightmap[y][x]
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT and (new_x, new_y) not in seen:
                    other_height = heightmap[new_y][new_x]
                    if other_height - height <= 1:
                        if (new_x, new_y) == END:
                            return steps
                        new_points.add((new_x, new_y))
        points = new_points

print(solve({START}))
print(solve(a))
