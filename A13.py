# わからん
N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(1, N):
    Left = 1
    Right = N - 1
    while Left < Right:
        mid = (Left + Right) // 2
        if A[mid] <= A[i] - K:
            Left = mid + 1
        if A[mid] > A[i] - K:
            Right = mid
    Answer = Left
    if Answer - i > 0:
        sum += (Answer - i)

print(sum)