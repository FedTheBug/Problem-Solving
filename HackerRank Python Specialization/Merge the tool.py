def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    # l = n//k
    s = ""
    t = ""
    for i in range(0, n - k + 1, k):
        s = string[i : i + k]
        for j in range(len(s)):
            if s[j] not in t:
                t = t + s[j]
        print(t)
        s = ""
        t = ""


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
