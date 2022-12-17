import itertools

with open('input.txt') as f:
    DIRECTIONS = {'<': -1, '>': 1}
    JETS = list(map(DIRECTIONS.get, f.read().rstrip()))

ROCKS = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)},
    {(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)},
    {(0, 3), (0, 2), (0, 1), (0, 0)},
    {(0, 1), (1, 1), (0, 0), (1, 0)},
]

jets  = itertools.cycle(JETS)
rocks = itertools.cycle(ROCKS)

landed = set()

for _ in range(2022):
    max_y = max((y for x, y in landed), default=-1)

    # rock appears
    rock = {(x + 2, y + max_y + 4) for x, y in next(rocks)}

    while True:
        # pushed by jet
        dx = next(jets)
        new_rock = set()
        for x, y in rock:
            new_x = x + dx
            if 0 <= new_x < 7 and (new_x, y) not in landed:
                new_rock.add((new_x, y))
            else:
                break
        else:
            rock = new_rock

        # fall down
        new_rock = set()
        for x, y in rock:
            new_y = y - 1
            if new_y >= 0 and (x, new_y) not in landed:
                new_rock.add((x, new_y))
            else:
                break
        else:
            rock = new_rock
            continue

        landed.update(rock)
        break

print(max(y for x, y in landed) + 1)
