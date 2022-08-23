d = [0] * 41
d[0] = [0, 1, 0]
d[1] = [1, 0, 1]
def fibo(N):
    if N == 1:
        return d[1]
    
    if d[N]:
        return d[N]
   
    d[N] = [fibo(N-1)[0] + fibo(N-2)[0], fibo(N-1)[1] + fibo(N-2)[1], fibo(N-1)[2] + fibo(N-2)[2]]
    return d[N]

T = int(input())

for _ in range(T):
    N = int(input())

    if N == 0:
        print(1, 0)
    else:
        fibo(N)

        print(d[N][1], d[N][2])

