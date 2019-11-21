W, S, C, K = map(int, input().split())

if S == 0:
    print("YES")
if W == 0:
    if K >= S:
        print("YES")

if C == 0 & K >= W:
    print("YES")
elif S == 0:
    print("YES")
elif W == 0 & K >= C:
    print("YES")
if S == 0:
    print("YES")

else:
    print("NO")
