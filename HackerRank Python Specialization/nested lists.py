if __name__ == "__main__":
    students = list()
    for _ in range(int(input())):
        students.append([input(), float(input())])
    print(students)
    students.sort(key=lambda x: (x[1], x[0]))
    print(students)
    name = [i[0] for i in students]
    score = [i[1] for i in students]
    lowest_score = min(score)
    # score.remove(lowest_score)
    # print(students)
    while score[0] == lowest_score:
        score.remove(score[0])
        name.remove(name[0])
    for i in range(0, len(score)):
        if score[i] == min(score):
            print(name[i])
