N = int(input())


def where_is_it(x, y):
    i = 1;
    j = 1
    while x > (2 ** i):
        i += 1
    while y > (2 ** j):
        j += 1

    return 1


for _ in range(N):
    x, y = map(int, input().split())
    where_is_it(x, y)
