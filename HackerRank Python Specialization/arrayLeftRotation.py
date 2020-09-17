#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(0, d):
        first = a[0]
        for j in range(0, len(a) - 1):
            a[j] = a[j + 1]
        a[len(a) - 1] = first
    return a


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    # print(a)
    result = rotLeft(a, d)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
