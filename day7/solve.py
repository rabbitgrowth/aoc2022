root = {}
dirs = [root]

with open('input.txt') as f:
    for line in f:
        words = line.split()
        if words[0] == '$':
            cmd, *args = words[1:]
            if cmd == 'cd':
                [name] = args
                if name == '..':
                    dirs.pop()
                else:
                    assert name not in dirs[-1]
                    dirs[-1][name] = new_dir = {}
                    dirs.append(new_dir)
        else:
            meta, name = words
            if meta != 'dir':
                dirs[-1][name] = int(meta)

def sizeof(dir_):
    return sum(v if isinstance(v, int) else sizeof(v)
               for v in dir_.values())

def sizes(dir_):
    for v in dir_.values():
        if isinstance(v, dict):
            yield sizeof(v)
            yield from sizes(v)

unused = 70_000_000 - sizeof(root)
needed = 30_000_000 - unused

print(sum(filter(lambda size: size <= 100_000, sizes(root))))
print(next(filter(lambda size: size >= needed, sorted(sizes(root)))))
