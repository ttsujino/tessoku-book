def kansu(x):
    return (x**3 + x)

N = int(input())

L = 0
R = N * 1000

while L < R:
    mid = (L + R) // 2
    mid_1000 = mid / 1000
    output = kansu(mid_1000)
    output_1000 = int(output * 1000)
    N_1000 = int(N * 1000)
    if output_1000 >= N_1000:
        R = mid
    elif output_1000 < N_1000:
        L = mid + 1

print(L / 1000)
