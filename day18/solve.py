import itertools

with open('input.txt') as f:
    points = {tuple(map(int, line.rstrip().split(','))) for line in f}

def get_neighbours(point):
    x, y, z = point
    yield (x - 1, y, z)
    yield (x + 1, y, z)
    yield (x, y - 1, z)
    yield (x, y + 1, z)
    yield (x, y, z - 1)
    yield (x, y, z + 1)

def get_surface_area(points):
    return sum(neighbour not in points
               for point in points
               for neighbour in get_neighbours(point))

print(get_surface_area(points))

# bounding box with 1 unit of empty space around the points
min_x = min(x for x, _, _ in points) - 1
max_x = max(x for x, _, _ in points) + 1
min_y = min(y for _, y, _ in points) - 1
max_y = max(y for _, y, _ in points) + 1
min_z = min(z for _, _, z in points) - 1
max_z = max(z for _, _, z in points) + 1

def within_bounds(cube):
    x, y, z = cube
    return (min_x <= x <= max_x
            and min_y <= y <= max_y
            and min_z <= z <= max_z)

outside = (min_x, min_y, min_z)

queue = [outside]
air   = {outside}
while queue:
    point = queue.pop(0)
    for neighbour in get_neighbours(point):
        if (within_bounds(neighbour)
                and neighbour not in points
                and neighbour not in air):
            queue.append(neighbour)
            air.add(neighbour)

for point in itertools.product(range(min_x, max_x + 1),
                               range(min_y, max_y + 1),
                               range(min_z, max_z + 1)):
    if point not in points and point not in air:
        points.add(point)

print(get_surface_area(points))
