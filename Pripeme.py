t = int(input())
a = input().split()
b = list()
for value in a:
    b.append(int(value))

if max(b) > (sum(b)-max(b)):
    print(2*max(b))
else:
    print(sum(b))