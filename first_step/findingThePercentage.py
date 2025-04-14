n = int(input())
student_mark = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_mark[name] = scores
    
query_name = input()
if query_name in  student_mark:
    score = student_mark[query_name]
    avg = sum(score)/len(score)
    print("{:.2f}".format(avg))
