N = int(input())
h = list(map(int, input().split()))

CostSum = [0] * (N + 1)

for i in range(1, N + 1):
    if i == 1:
        CostSum[i] = 0
    if i == 2:
        CostSum[i] = abs(h[0] - h[1])
    if i > 2:
        CostSum[i] = min(
            CostSum[i - 2] + abs(h[i - 3] - h[i - 1]),
            CostSum[i - 1] + abs(h[i - 2] - h[i - 1])    
        )

print(CostSum[N])