from collections import namedtuple

n = int(input())
categories = input().split()
total = 0

for i in range(n):
    Student = namedtuple("Student", categories)
    cat1, cat2, cat3, cat4 = input().split()
    Student = Student(cat1, cat2, cat3, cat4)
    total += int(Student.MARKS)

print("{0:.2f}".format(total / n))

