# xu li tap tin

with open("text.txt") as f:
    # print(f.read(5)) #doc va in ra man hinh text
    for x in f:
        print(x)
# fa = open("text.txt")
# print(fa.readline(1))
# fa.close()

# with open("text.txt", "w") as fa:
#     fa.write("\nHello World!")
#     fa.write("\nHello World 2!")
fa = open("text.txt")
myString = fa.read()
fa.close()
print(myString[0:5])  # This will not work as `str` has no method `subString`

fa