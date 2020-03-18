def solve(s):

    lst = s.split(" ")
    # string = " "
    return " ".join(i.capitalize() for i in lst)


if __name__ == "__main__":
    s = input()
    result = solve(s)
    print(result)

