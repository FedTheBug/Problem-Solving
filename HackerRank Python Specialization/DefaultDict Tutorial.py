from collections import defaultdict

d = defaultdict(list)
list1 = []
list2 = []
n, m = map(int, input().split())
# print(m, n)
for i in range(n):
    d[input()].append(i + 1)
# print(d)
for i in range(m):
    list1.append(input())
# print(list1)
for i in list1:
    if i in d:
        print(" ".join(map(str, d[i])))
        # print(d[i])
    else:
        print(-1)
