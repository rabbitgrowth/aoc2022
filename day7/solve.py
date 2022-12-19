from collections import Counter

sizes = Counter()
cwd = []

def prefixes(dirs):
    prefix = []
    for dir_ in dirs:
        prefix.append(dir_)
        yield tuple(prefix)

with open('input.txt') as f:
    for line in f:
        words = line.split()
        if words[0] == '$':
            if words[1] == 'cd':
                name = words[2]
                if name == '..':
                    cwd.pop()
                else:
                    cwd.append(name)
        else:
            meta = words[0]
            if meta != 'dir':
                size = int(meta)
                for prefix in prefixes(cwd):
                    sizes[prefix] += size

unused = 70000000 - sizes[('/',)]
needed = 30000000 - unused

print(sum(filter(lambda size: size <= 100000, sizes.values())))
print(next(filter(lambda size: size >= needed, sorted(sizes.values()))))
