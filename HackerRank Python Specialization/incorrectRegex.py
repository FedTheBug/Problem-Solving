import re

for _ in range(int(input())):
    # is_valid = True
    try:
        re.compile(input())
        print("True")
    except re.error:
        s_valid = False
        print("False")

