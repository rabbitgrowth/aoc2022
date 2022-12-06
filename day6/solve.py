from collections import deque

with open('input.txt') as f:
    line = f.read().rstrip()

for n in (4, 14):
    window = deque(maxlen=n)
    for i, char in enumerate(line):
        window.append(char)
        if len(window) == len(set(window)) == window.maxlen:
            print(i + 1)
            break
