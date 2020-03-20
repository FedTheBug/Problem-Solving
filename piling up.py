for i in range(int(input())):
    (int(input()))
    lst = list(map(int, input().split()))
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i + 1]:
        i += 1
        # print("first", i)
    while i < l - 1 and lst[i] <= lst[i + 1]:
        i += 1
        # print("second", i)
    if i == l - 1:
        print("Yes")
    else:
        print("No")
