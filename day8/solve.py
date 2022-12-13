with open('input.txt') as f:
    trees = [list(map(int, line.rstrip())) for line in f]

WIDTH  = len(trees[0])
HEIGHT = len(trees)

visible   = 0
max_score = 0

for y, row in enumerate(trees):
    for x, tree in enumerate(row):
        lines = []
        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            line = []
            new_x, new_y = x, y
            while True:
                new_x += dx
                new_y += dy
                if not (0 <= new_x < WIDTH and 0 <= new_y < HEIGHT):
                    break
                line.append(trees[new_y][new_x])
            lines.append(line)

        for line in lines:
            for other_tree in line:
                if other_tree >= tree:
                    break
            else:
                visible += 1
                break

        score = 1
        for line in lines:
            distance = 0
            for distance, other_tree in enumerate(line, 1):
                if other_tree >= tree:
                    break
            score *= distance
        if score > max_score:
            max_score = score

print(visible)
print(max_score)
