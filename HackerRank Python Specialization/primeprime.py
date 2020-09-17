n = int(input())
res = list()
for _ in range(n):
    name, num = input().split()
    num = int(num)
    x = 0
    l = list()
    # res = list()
    ns = [ord(c) for c in name]
    for i in ns:
        x = i + num
        l.append(x)
    # print(l)
    for k in range(len(l)):
        f = int(l[k])
        if f > 1:
            for i in range(2, f):
                if (f % i) == 0:
                    res.append("NO")
                    break
            else:
                res.append("YES")
                break

        else:
            res.append("NO")
        break
# print(res)
# for r in res:
#     print(*r, "\n")
print("\n".join(res))
