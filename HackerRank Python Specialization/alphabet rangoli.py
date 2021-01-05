def print_rangoli(size):
    # your code goes here
    string = "abcdefghijklmnopqrstuvwxyz"[0:size]
    for i in range(size - 1, -size, -1):
        x = abs(i)
        line = string[size:x:-1] + string[x:size]
        print("--" * x + "-".join(line) + "--" * x)


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)
