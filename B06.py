N = int(input())
A = map(int, input().split())
Q = int(input())

SumList = []
Sum = 0
SumList.append(Sum)
for i in A:
    Sum += i
    SumList.append(Sum)

for i in range(Q):
    L, R = map(int, input().split())
    Num = SumList[R] - SumList[L - 1]
    if Num == (R - L + 1) / 2:
        print("draw")
    elif Num > (R - L + 1) / 2:
        print("win")
    else:
        print("lose")

# 考察
# 相変わらず[None] * で先にリストを作ってる