def search_index(p, Q):
    Left = 0
    Right = len(Q) - 1
    while Left < Right:
        mid = (Left + Right) // 2
        if p <= Q[mid]:
            Right = mid
        if p > Q[mid]:
            Left = mid + 1
    return Left

N = int(input())
A = list(map(int, input().split()))

B = []
A_new = sorted(list(set(A)))
for i in A:
    B.append(search_index(i, A_new) + 1)
print(*B)