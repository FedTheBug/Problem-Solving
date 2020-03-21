from itertools import product

K, M = map(int, input().split())
lst = []
for _ in range(K):
    lst.append([int(x) for x in input().split()][1:])

comb = list(product(*lst))


def fun(nums):
    return sum(x * x for x in nums) % M


print(max(list(map(fun, comb))))
