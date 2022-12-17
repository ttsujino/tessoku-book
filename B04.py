N = input()
N = list(N)
N.reverse()

num = 0
for i, v in enumerate(N):
    new = 2 ** i * int(v)
    num += new

print(num)

# >考察
# こんな遠回りなやり方しなくてもrange(len(N))してN[i]すればいい
