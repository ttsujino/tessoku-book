def check(x, N, K, A):
    # xがKより大きかったらTrue,小さかったらFalseを返す
    sum = 0
    for i in range(N):
        sum += x // A[i]
    
    if sum >= K:
        return True
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 1
R = 10 ** 9

while L < R:
    mid = (L + R) // 2
    status = check(mid, N, K, A)

    if status:
        R = mid
    elif not status:
        L = mid + 1
    else:
        raise NotImplementedError("code is wrong")

print(L)