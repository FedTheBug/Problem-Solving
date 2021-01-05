n = int(input())
a = list(map(int, input().split()))
a = set(a)

for i in range(int(input())):
    key = input().split()
    if key[0] == "pop":
        a.pop()
    elif key[0] == "remove":
        a.remove(int(key[1]))
    elif key[0] == "discard":
        a.discard(int(key[1]))

print(sum(s))
