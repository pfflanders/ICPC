N, Q = input().split()
N = int(N)
Q = int(Q)
R = list(map(int, input().split()))
C = list(map(int, input().split()))


def find_path(x, y, u, v, shit, shit2):

    if x == u and y == v:
        return True

    else:
        if x + 1 < N and (R[x + 1] + C[y]) % 2 == 0 and x + 1 != shit:
            if find_path(x + 1, y, u, v, x, y):
                return True
        if x - 1 >= 0 and (R[x - 1] + C[y]) % 2 == 0 and x - 1 != shit:
            if find_path(x - 1, y, u, v, x, y):
                return True
        if y + 1 < N and (R[x] + C[y + 1]) % 2 == 0 and y + 1 != shit2:
            if find_path(x, y + 1, u, v, x, y):
                return True
        if y - 1 >= 0 and (R[x] + C[y - 1]) % 2 == 0 and y - 1 != shit2:
            if find_path(x, y - 1, u, v, x, y):
                return True
    return False


for i in range(Q):
    a, b, c, d = map(int, input().split())
    if find_path(a-1, b-1, c-1, d-1, -1, -1):
        print("YES")
    else:
        print("NO")
