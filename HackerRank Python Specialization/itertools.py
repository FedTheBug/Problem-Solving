from itertools import product

A = list(map(int, input().split()))
# print(A)
B = list(map(int, input().split()))
print(*product(A, B))

