N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S + 1) for _ in range(N + 1)]

dp[0][0] = True

for i in range(1, N + 1):
    for j in range(S + 1):
        if j < A[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True
        else:
            if (dp[i - 1][j] == True) or (dp[i - 1][j - A[i - 1]] == True):
                dp[i][j] = True

Answer = "No"
for i in range(N + 1):
    if dp[i][S] == True:
        Answer = "Yes"

print(Answer)
