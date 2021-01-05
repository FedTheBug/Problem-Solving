from itertools import combinations

N = int(input())
L = input().split()
K = int(input())

C = list(combinations(L, K))
C_f = list(filter(lambda x: "a" in x, C))
prob = len(C_f) / len(C)
print("{0:.3}".format(prob))

