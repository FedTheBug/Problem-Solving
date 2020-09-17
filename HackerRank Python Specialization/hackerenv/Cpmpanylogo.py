from collections import Counter

sequence = input()
[print(*c) for c in Counter(sorted(sequence)).most_common(3)]