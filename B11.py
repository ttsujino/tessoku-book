# bisectが自分で実装できない
# 下記は間違ってる解法
def search(x, A):
    L = 0
    R = N - 1
    while L < R:
        M = (L + R) // 2
        if x <= A[M]:
            R = M
        else:
            L = M + 1
        if R == L:
            return R

N = int(input())
A = list(map(int, input().split()))
A.sort
Q = int(input())
X = [None] * Q
for i in range(Q):
    X[i] = int(input())

for i in range(Q):
    Answer = search(X[i], A)
    print(Answer)
