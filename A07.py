# TLEの回答
D = int(input())
N = int(input())

sanka = [0] * D
for _ in range(N):
    L, R = map(int, input().split())
    for i in range(L - 1, R):
        sanka[i] = sanka[i] + 1

for j in sanka:
    print(j)


# TLEの回答2
D = int(input())
N = int(input())

sanka = [0] * D
pls = lambda a, b: a + b
for _ in range(N):
    L, R = map(int, input().split())
    sanka_ind = [0] * D
    sanka_ind[L-1:R] = [1] * (R - L)
    sanka = map(pls, sanka, sanka_ind)

for j in sanka:
    print(j)


# 正解の回答
D = int(input())
N = int(input())
L = [0] * N
R = [0] * N
for i in range(N):
	L[i], R[i] = map(int, input().split())

sanka = [0] * (D + 2)
for i in range(N):
    sanka[L[i]] += 1
    sanka[R[i] + 1] -= 1

answer = [0] * (D + 2)
for i in range(1, D + 1):
    answer[i] = answer[i - 1] + sanka[i]

for i in range(1, D + 1):
    print(answer[i])

# 考察
# sum(list[:*])はfor文回してるのと一緒