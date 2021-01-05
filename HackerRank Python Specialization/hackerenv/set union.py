from collections import Counter

n = int(input())
a = list(map(int, input().split()))[:n]
a = set(a)
m = int(input())
b = list(map(int, input().split()))[:m]
b = set(b)
c = a.union(b)
print(len(c))
