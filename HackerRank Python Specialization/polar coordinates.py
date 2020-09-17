import cmath

inp = complex(input())
res = cmath.polar(inp)
print(*res, sep="\n")
