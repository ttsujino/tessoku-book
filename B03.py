n = int(input())
a = list(map(int, input().split()))

answer = "No"

for i in range(len(a - 2)):
    for j in range(i + 1, len(a - 1)):
        for k in range(j + 1, len(a)):
            if (a[i] + a[j] + a[k]) == 1000:
                answer = "Yes"
        
print(answer)
