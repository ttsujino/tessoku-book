N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

Time = [0] * N

for i in range(N):
    if i == 0:
        Time[i] = 0
    if i == 1:
        Time[i] = A[i - 1]
    if i > 1:
        Time[i] = min(Time[i - 1] + A[i - 1], Time[i - 2] + B[i - 2])

Answer = []
Place = N - 1

while True:
    Answer.append(Place + 1)
    if Place == 0:
        break
    if Time[Place] == Time[Place - 1] + A[Place - 1]:
        Place -= 1
    else:
        Place -= 2

Answer.reverse()

print(len(Answer))
print(*Answer)

