import functools
import itertools
import json
import math

def compare(l, r):
    types = tuple(map(type, (l, r)))
    if types == (list, list):
        for ll, rr in itertools.zip_longest(l, r):
            if ll is None:
                return -1
            if rr is None:
                return 1
            result = compare(ll, rr)
            if result:
                return result
    elif types == (int, int):
        return (l > r) - (l < r)
    elif types == (list, int):
        return compare(l, [r])
    elif types == (int, list):
        return compare([l], r)

with open('input.txt') as f:
    pairs = [tuple(map(json.loads, par.splitlines())) for par in f.read().split('\n\n')]

print(sum(i for i, (l, r) in enumerate(pairs, 1) if compare(l, r) == -1))

DIVIDERS = [[[2]], [[6]]]
packets = [packet for pair in pairs for packet in pair] + DIVIDERS
sorted_packets = sorted(packets, key=functools.cmp_to_key(compare))
print(math.prod(sorted_packets.index(divider) + 1 for divider in DIVIDERS))
