N = int(input())
h = list(map(int, input().split()))

CostSum = [0] * (N)

for i in range(0, N):
    if i == 0:
        CostSum[i] = 0
    if i == 1:
        CostSum[i] = abs(h[0] - h[1])
    if i > 1:
        CostSum[i] = min(
            CostSum[i - 2] + abs(h[i - 2] - h[i]),
            CostSum[i - 1] + abs(h[i - 1] - h[i])    
        )

Place = N - 1
Answer = []

while True:
    Answer.append(Place + 1)
    if Place == 0:
        break
    if CostSum[Place] == CostSum[Place - 1] + abs(h[Place - 1] - h[Place]):
        Place -= 1
    else:
        Place -= 2

Answer.reverse()
print(len(Answer))
print(*Answer)