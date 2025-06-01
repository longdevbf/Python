# xu li tap tin

with open("text.txt") as f:
    # print(f.read(5)) #doc va in ra man hinh text
    for x in f:
        print(x)
# fa = open("text.txt")
# print(fa.readline(1))
# fa.close()

with open("text.txt", "a") as fa:
    fa.write