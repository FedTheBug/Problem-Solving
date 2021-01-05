from itertools import product

K, M = map(int, input().split())
# print("M", M)
# lst = []
lst = (list(map(int, input().split()))[1:] for _ in range(K))

# max_lst = [max(x) for x in lst]
# print("max_lst", max_lst)
# max_lst_square = [pow(x, 2) for x in max_lst]
# print("max_lst_square", max_lst_square)
# print("SUM", sum(max_lst_square))
# s = sum(max_lst_square)
results = map(lambda x: sum(i ** 2 for i in x) % M, product(*lst))
# print(list(results))
# res = s % M


print(max(results))
