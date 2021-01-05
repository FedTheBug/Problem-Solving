#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt = s.count("a") * (n // len(s))
    rem = s[: n % len(s)].count("a")
    return cnt + rem


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
