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
            cmd, *args = words[1:]
            if cmd == 'cd':
                [name] = args
                if name == '..':
                    cwd.pop()
                else:
                    cwd.append(name)
        else:
            meta, name = words
            if meta != 'dir':
                size = int(meta)
                for prefix in prefixes(cwd):
                    sizes[prefix] += size

unused = 70_000_000 - sizes[('/',)]
needed = 30_000_000 - unused

print(sum(filter(lambda size: size <= 100_000, sizes.values())))
print(next(filter(lambda size: size >= needed, sorted(sizes.values()))))