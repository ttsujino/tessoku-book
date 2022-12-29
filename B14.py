import sys
import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))

mid = N // 2

P = A[:mid]
Q = A[mid:]

PS = [0] * len(P)
P_conb = []
for i in range(1<<len(P)):
    use = [False] * len(P)
    for j in range(len(P)):
        if i & (1<<j):
            use[j] = True
    sum_ = 0
    for j in range(len(P)):
        if use[j]:
            sum_ += P[j]
    P_conb.append(sum_)
    
Q_conb = []
for i in range(1<<len(Q)):
    use = [False] * len(Q)
    for j in range(len(Q)):
        if i & (1<<j):
            use[j] = True
    sum_ = 0
    for j in range(len(Q)):
        if use[j]:
            sum_ += Q[j]
    Q_conb.append(sum_)
    
P_conb.sort()
Q_conb.sort()

for i in P_conb:
    target = bisect.bisect_left(Q_conb, K - i)
    if target < len(Q_conb) and Q_conb[target] == K - i:
        print("Yes")
        sys.exit(0)

print("No")