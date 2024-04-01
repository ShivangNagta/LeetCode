a = "hello world  "
ansList = a.split(" ")
print(ansList)
n = -1
while ansList[n] == "":
    print(n)
    n = n - 1
print(ansList[n])