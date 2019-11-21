t = int(input())

mySolution = ""
original = input()
for i in original:
    mySolution += (str(t - int(i) + 1))
print(mySolution)
