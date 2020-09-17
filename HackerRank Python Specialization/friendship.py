n = int(input())
for _ in range(n):
    n, m = input().split()
    n = int(n)
    m = int(m)
    nlist = list()
    mlist = list()
    for i in range(1, n + 1):
        if n % i == 0:
            nlist.append(i)
    for j in range(1, m + 1):
        if m % j == 0:
            mlist.append(j)
    nlist.remove(n)
    mlist.remove(m)

    nbigsum = 0
    mbigsum = 0
    for nl in nlist:
        nbigsum += nl
    # print(nbigsum)
    for ml in mlist:
        mbigsum += ml
    # print(mbigsum)
    if nbigsum == m and mbigsum == n:
        print("Friendship is ideal")
    else:
        print("Friendship is not ideal")
