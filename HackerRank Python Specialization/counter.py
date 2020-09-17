import collections

x = int(input())
size = collections.Counter(map(int, input().split()))
# print(size)
# print(list(size.items()))
numcustomer = int(input())
earned = 0
for i in range(numcustomer):
    s_size, price = map(int, input().split())
    if size[s_size]:
        earned += price
        size[s_size] -= 1

print(earned)

