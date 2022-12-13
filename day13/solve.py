import itertools
import json
import math

def compare(l, r):
    types = tuple(map(type, (l, r)))
    if types == (list, list):
        for ll, rr in itertools.zip_longest(l, r):
            if ll is None:
                return True
            if rr is None:
                return False
            result = compare(ll, rr)
            if result is not None:
                return result
    elif types == (int, int):
        if l < r:
            return True
        elif l > r:
            return False
    elif types == (list, int):
        return compare(l, [r])
    elif types == (int, list):
        return compare([l], r)

with open('input.txt') as f:
    pairs = [tuple(map(json.loads, par.splitlines()))
             for par in f.read().split('\n\n')]

print(sum(i
          for i, (l, r) in enumerate(pairs, 1)
          if compare(l, r)))

DIVIDERS = [[[2]], [[6]]]

sorted_packets = DIVIDERS[::]

for pair in pairs:
    for packet in pair:
        for i, sorted_packet in enumerate(sorted_packets):
            if compare(packet, sorted_packet):
                sorted_packets.insert(i, packet)
                break
        else:
            sorted_packets.append(packet)

print(math.prod(sorted_packets.index(divider) + 1
                for divider in DIVIDERS))
