if __name__ == "__main__":
    n = int(input())
    students_mark = {}
    for _ in range(n):
        name, *marks = input().split()
        scores = list(map(float, marks))
        students_mark[name] = scores
    query_name = input()
    # print(query_name)
    target = students_mark[query_name]
    # avg = [sum(i) / 3 for i in target]
    print("%.2f" % (sum(target) / 3))
    # print(avg)
