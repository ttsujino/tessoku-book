T = int(input())
N = int(input())
kintai = [0] * (T + 1)

for i in range(N):
    L, R = map(int, input().split())
    kintai[L] += 1
    kintai[R] -= 1

answer = []
working = 0
for j in kintai:
    working += j
    answer.append(working)

for k in range(len(answer) - 1):
    print(answer[k])
