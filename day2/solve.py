score1 = 0
score2 = 0

with open('input.txt') as f:
    for line in f:
        l, r = line.split()
        a = 'ABC'.index(l)
        b = 'XYZ'.index(r)
        score1 += ((b - a + 1) % 3) * 3
        score1 += b + 1
        score2 += ((a + b - 1) % 3) + 1
        score2 += b * 3

print(score1)
print(score2)
