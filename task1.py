#!/usr/bin/env python
n = int(input())
students = {}
for i in range(n):
    name, *args = input().split()
    avg_mark = sum(list(map(float, args))) / 3
    k = {name: avg_mark}
    students.update(k)
name_student = input()
print('%.2f' % students[name_student])
