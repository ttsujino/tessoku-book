N, Q = map(int, input().split())
A = list(map(int, input().split()))

Asum = 0
Asum_list = []
for a in A:
    Asum += a
    Asum_list.append(Asum)

for _ in range(Q):
    L, R = map(int, input().split())
    if L > 1:
      answer = Asum_list[R - 1] - Asum_list[L - 2]
    else:
      answer = Asum_list[R - 1]
    print(answer)


# 解2
N, Q = map(int, input().split())
A = list(map(int, input().split()))

Asum = 0
Asum_list = []
Asum_list.append(Asum)
for a in A:
    Asum += a
    Asum_list.append(Asum)

for _ in range(Q):
    L, R = map(int, input().split())
    answer = Asum_list[R] - Asum_list[L - 1]
    print(answer)

# >考察
# 累計和ははじめにリストを作ってから差を計算する
# 解2の方が実行時間ちょっと長かった