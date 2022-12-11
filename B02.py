a, b = map(int, input().split())

answer = "No"
for i in range(a, b + 1):
    if 100 % i == 0:
        answer = "Yes"
        break

print(answer)
