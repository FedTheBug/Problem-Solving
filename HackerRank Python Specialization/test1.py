if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for i in range(n)]
    print(nums)
    k = int(input())

    nums.sort(key=lambda x: x[k])
    print(nums)

    for line in nums:
        print(*line, sep=" ")

