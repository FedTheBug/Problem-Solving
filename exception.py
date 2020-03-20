for _ in range(int(input())):

    try:
        a, b = map(int, input().split(" "))
        print(int(a) // int(b))
    except Exception as e:
        print("Error Code: ", e)
