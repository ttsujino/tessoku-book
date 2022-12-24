N = int(input())
A = list(map(int, input().split()))
D = int(input())
MaxFromLeft = [0] * (N + 2)
MaxFromRight = [0] * (N + 2)

for i in range(1, N + 1):
    MaxFromLeft[i] = max(MaxFromLeft[i - 1], A[i - 1])
    MaxFromRight[-i - 1] = max(MaxFromRight[-i], A[-i])

for i in range(D):
    L, R = map(int, input().split())
    Answer = max(MaxFromLeft[L - 1], MaxFromRight[R + 1])
    print(Answer)