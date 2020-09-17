from itertools import groupby

s = input()
for key, value in groupby(s):
    print((len(list(value)),int(key)), end=" ")
# for key, value in groupby(s):
#     print(type(key), type(value), end=" ")

