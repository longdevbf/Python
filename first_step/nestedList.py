n = int(input())
list_student = []
list_name = []
list_grade = []
for i in range(n):
    name = input()
    grade = float(input())
    list_student.append([name, grade])
list_student.sort(key=lambda x: x[1])
# print(list_student)
min = list_student[0][1]
temp = 0
cnt = 0
for i in range(n):
    if(list_student[i][1] != min):
        temp = list_student[i][1]
        break
for i in range(n):
    if(list_student[i][1] == temp):
        cnt += 1
result = []
if(cnt > 1):
    list_name.sort(key=lambda x: x[0])
    for i in range(n):
        if(list_student[i][1] == temp):
            result.append(list_student[i][0])
else:
    for i in range(n):
        if(list_student[i][1] == temp):
            result.append(list_student[i][0])
result.sort()
for i in range(len(result)):
    print(result[i])
