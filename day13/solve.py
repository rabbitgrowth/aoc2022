import itertools
import math

def compare(l, r):
    if all(isinstance(x, list) for x in (l, r)):
        for ll, rr in itertools.zip_longest(l, r):
            if ll is None:
                return True
            if rr is None:
                return False
            result = compare(ll, rr)
            if result is not None:
                return result
    elif all(isinstance(x, int) for x in (l, r)):
        if l < r:
            return True
        elif l > r:
            return False
    elif isinstance(l, list):
        return compare(l, [r])
    else:
        return compare([l], r)

with open('input.txt') as f:
    pairs = [list(map(eval, par.splitlines()))
             for par in f.read().split('\n\n')]

print(sum(i
          for i, (l, r) in enumerate(pairs, 1)
          if compare(l, r)))

DIVIDERS = [[[2]], [[6]]]

sorted_packets = DIVIDERS[::]

for pair in pairs:
    for packet in pair:
        try:
            i = next(i
                     for i, sorted_packet in enumerate(sorted_packets)
                     if compare(packet, sorted_packet))
            sorted_packets.insert(i, packet)
        except StopIteration:
            sorted_packets.append(packet)

print(math.prod(sorted_packets.index(divider) + 1
                for divider in DIVIDERS))
