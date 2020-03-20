d = dict()

for i in range(int(input())):
    key = input()
    if not key in d.keys():
        d.update({key: 1})
        continue
    d[key] += 1


print(len(d))
print(*d.values())
