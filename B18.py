N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S + 1) for i in range(N + 1)]

dp[0][0] = True
for i in range(1, N + 1):
    for j in range(S + 1):
        if j < A[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True
        if j >= A[i - 1]:
            if (dp[i - 1][j] == True) or (dp[i - 1][j - A[i - 1]] == True):
                dp[i][j] = True

if dp[N][S] == False:
    print("-1")
    import sys
    sys.exit(0)

Place = S
Answer = []

for i in reversed(range(1, N + 1)):
    if dp[i - 1][Place] == True:
        pass
    else:
        Answer.append(i)
        Place = Place - A[i - 1]

Answer.reverse()

print(len(Answer))
print(*Answer)
