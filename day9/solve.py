DIRECTIONS = {
    'U': ( 0, -1),
    'D': ( 0,  1),
    'L': (-1,  0),
    'R': ( 1,  0),
}

with open('input.txt') as f:
    motions = []
    for line in f:
        a, b = line.split()
        direction = DIRECTIONS[a]
        steps = int(b)
        motions.append((direction, steps))

def sign(x):
    return (x > 0) - (x < 0)

for length in (2, 10):
    rope = [(0, 0)] * length
    visited = set()
    for (dx, dy), steps in motions:
        for _ in range(steps):
            new_rope = []
            x, y = rope[0]
            x += dx
            y += dy
            new_rope.append((x, y))
            for curr_x, curr_y in rope[1:]:
                dst = (curr_x + sign(x - curr_x),
                       curr_y + sign(y - curr_y))
                if dst != (x, y):
                    curr_x, curr_y = dst
                new_rope.append((curr_x, curr_y))
                x = curr_x
                y = curr_y
            visited.add((x, y))
            rope = new_rope
    print(len(visited))
