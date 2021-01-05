import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    swapc = 0
    for i in range(len(arr)):
        while arr[i] != i + 1:
            temp = arr[i]
            arr[i] = arr[arr[i] - 1]
            arr[arr[i] - 1] = temp
            swapc += swapc + 1

    return swapc


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)

    # fptr.write(str(res) + '\n')

    # fptr.close()
