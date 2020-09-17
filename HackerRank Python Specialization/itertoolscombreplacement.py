from itertools import combinations_with_replacement

a, b = input().split()
a = sorted(a)
b = int(b)
lis = []
# for _ in range(1, b + 1):
lis += list(combinations_with_replacement(a, b))
for i in lis:
    print("".join(i))
