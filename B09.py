N = int(input())
A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N

for n in range(N):
    A[n], B[n], C[n], D[n] = map(int, input().split())

S = [[0] * (1501) for i in range((1501))]

for i in range(N):
    S[A[i]][B[i]] += 1
    S[A[i]][D[i]] -= 1
    S[C[i]][B[i]] -= 1
    S[C[i]][D[i]] += 1

for i in range(0, 1501):
	for j in range(1, 1501):
		S[i][j] = S[i][j-1] + S[i][j]
for i in range(1, 1501):
	for j in range(0, 1501):
		S[i][j] = S[i-1][j] + S[i][j]

area = 0
for i in range(1501):
    for j in range(1501):
        if S[i][j] > 0:
            area += 1

print(area)
