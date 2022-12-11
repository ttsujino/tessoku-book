n, x = map(int, input().split())
a = list(map(int, input().split()))

answer = "No"

for i in a:
    if i == x:
        answer = "Yes"
        break

print(answer)
