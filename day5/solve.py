import re

def identity(x):
    return x

with open('input.txt') as f:
    par1, par2 = map(str.splitlines, f.read().split('\n\n'))

for function in (reversed, identity):
    stacks = [[] for _ in range((len(par1[0]) + 1) // 4)]
    for line in reversed(par1[:-1]):
        for i, stack in enumerate(stacks):
            item = line[i * 4 + 1]
            if item != ' ':
                stack.append(item)
    for line in par2:
        x, y, z = map(int, re.findall('\d+', line))
        items = stacks[y - 1][-x:]
        stacks[y - 1] = stacks[y - 1][:-x]
        stacks[z - 1].extend(function(items))
    print(''.join(stack[-1] for stack in stacks))
