
a = [1, 0]
b = [0, 1]

for i in range(2, 41):
    x = a[i - 1] + a[i - 2]
    y = b[i - 1] + b[i - 2]
    a.append(x)
    b.append(y)

T = int(input())

for i in range(T):
    N = int(input())
    print(a[N], b[N])
