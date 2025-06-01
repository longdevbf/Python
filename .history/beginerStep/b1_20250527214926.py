# xu li tap tin

with open("text.txt") as f:
    print(f.read()) #doc va in ra man hinh text

fa = open("text.txt", "w")
print(fa.readline())
fa.close()
