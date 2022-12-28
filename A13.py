N, K = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N - 1):
    Left = 1
    Right = N
    while Left < Right:
        mid = (Left + Right) // 2
        if A[mid] <= A[i] + K:
            Left = mid + 1
        if A[mid] > A[i] + K:
            Right = mid
    Answer = Left
    sum += (Answer - i - 1)

print(sum)

# 尺取り法
N, K = map(int, input().split())
A = list(map(int, input().split()))
R = [0] * N

Answer = 0
for i in range(N - 1):
    if i == 0:
        R[i] = 0
    if i >= 0:
        R[i] = R[i - 1]
    
    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

Answer = 0
for i in range(N - 1):
    Answer += (R[i] - i)
    
print(Answer)