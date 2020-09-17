def mutate_string(s, i, c):
    l = list(s)
    l[i] = c
    new_string = "".join(l)
    # print(type(l))
    # new_string = str(l)
    return new_string


if __name__ == "__main__":
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
