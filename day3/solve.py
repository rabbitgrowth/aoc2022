import string

ALPHABET = string.ascii_lowercase + string.ascii_uppercase

score1 = 0
score2 = 0

with open('input.txt') as f:
    for line in map(str.rstrip, f):
        half = len(line) // 2
        a = line[:half]
        b = line[half:]
        (common,) = set(a) & set(b)
        score1 += ALPHABET.index(common) + 1

with open('input.txt') as f:
    for lines in zip(f, f, f):
        a, b, c = map(str.rstrip, lines)
        (common,) = set(a) & set(b) & set(c)
        score2 += ALPHABET.index(common) + 1

print(score1)
print(score2)
