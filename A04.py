n = int(input())

digit = []
for i in range(10):
    digit.append(n % 2)
    n = n // 2

digit.reverse()
ans = "".join(map(str, digit))
ans.rjust(10, "0")
print(ans)

# >考察
# - 桁が決まっているときは桁ごとに出力
# - print()にend=''を指定することで改行なしのprintにできる