from collections import deque

d = deque()
for _ in range(int(input())):
    key = input().split()
    if key[0] == "append":
        d.append(int(key[1]))
    elif key[0] == "appendleft":
        d.appendleft(int(key[1]))
    elif key[0] == "pop":
        d.pop()
    elif key[0] == "popleft":
        d.popleft()

print(*d)

