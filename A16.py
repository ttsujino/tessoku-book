N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S = [None] * N
for i in range(N):
    if i == 0:
        S[i] = 0
    elif i == 1:
        S[i] = A[i - 1]
    else:
        S[i] = min(A[i - 1] + S[i - 1], B[i - 2] + S[i - 2])

print(S[N - 1])