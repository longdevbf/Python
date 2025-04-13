n = int(input())
arr = list(map(int, input().split()))
# select sort
checkBool = True

while(checkBool):
   checkBool = False
   for i in range(n):
       if  i != n - 1 and arr[i] > arr[i + 1]:
           arr[i], arr[i + 1] = arr[i + 1], arr[i]
           checkBool = True
    

# choose the max
max = arr[n - 1]
    
for i in range(n-1, -1, -1):
    if(arr[i] != max):
        print(arr[i])
        break
        