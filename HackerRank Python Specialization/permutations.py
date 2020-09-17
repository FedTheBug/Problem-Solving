from itertools import permutations

string, d = input().split()
print(*["".join(i) for i in permutations(sorted(string), int(d))], sep="\n")

