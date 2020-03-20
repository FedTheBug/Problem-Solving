from itertools import combinations
N = int(input())
lst = input().split(" ")
K = int(input())

lst1 = list(combinations(lst,k))
print(lst1)
f = filter(lambda x: 'a' in lst1,lst1)
print(f)