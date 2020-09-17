from itertools import combinations

if __name__ == "__main__":
    name, num = input().split()
    name = sorted(name)
    num = int(num)
    lis = []
    # print(name, num)
    # print(combinations(list(name), 1))
    for i in range(1, num + 1):
        lis += list(sorted(combinations(name, i)))
        print("LIST=>", lis)
    for i in lis:
        print("".join(i))

