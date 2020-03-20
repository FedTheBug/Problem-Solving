n, m = map(int, input().split())

arr = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

happiness = 0

for i in arr:
    if i in set1:
        happiness = happiness + 1
    elif i in set2:
        happiness = happiness - 1

print(happiness)
