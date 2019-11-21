N = int(input())
largestLxW = [0, 0]
secondLargestLxW = [0, 0]
for case in range(N):
    l, w = map(int, input().split())
    print(l, w)
    if l*w > largestLxW[0]*largestLxW[1]:
        secondLargestLxW = largestLxW
        largestLxW = [l, w]
        print("swap")

    elif l*w > secondLargestLxW[0]*secondLargestLxW[1]:
        secondLargestLxW = l * w

print(largestLxW)
print(secondLargestLxW)
if largestLxW[0]*largestLxW[1] > 2 * secondLargestLxW[0] * secondLargestLxW[1]:
    print(largestLxW[0]*largestLxW[1]*0.5)
else:

    A = secondLargestLxW
    if largestLxW[0] < largestLxW[1]:
        if largestLxW[0] < A[0]:
            A[0] = largestLxW
        elif largestLxW[0] < A[1]:
            A[1] = largestLxW[0]
    else:
        if largestLxW[1] < A[0]:
            A[0] = largestLxW
        elif largestLxW[1] < A[1]:
            A[1] = largestLxW[0]
    print(A[0]*A[1])
    print(A[0], A[1])
