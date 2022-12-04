import re

count1 = 0
count2 = 0

with open('input.txt') as f:
    for line in f:
        a, b, c, d = map(int, re.findall('\d+', line))
        count1 += a >= c and b <= d or a <= c and b >= d
        count2 += b >= c and a <= d

print(count1)
print(count2)
