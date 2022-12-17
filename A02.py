N, K = map(int, input().split())
 
answer = 0
for i in range(1, N + 1):
  if i < K:
    for j in range(1, N + 1):
      k = K - i - j
      if 1 <= k <= N: 
        answer += 1
 
print(answer)
