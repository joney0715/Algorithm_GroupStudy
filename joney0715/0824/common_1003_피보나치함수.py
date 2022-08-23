# 과거 계산 이력을 넣을 리스트
d = [0] * 41

# 피보나치 수열, 0 호출횟수, 1호출횟수
d[0] = [0, 1, 0]
d[1] = [1, 0, 1]

def fibo(N):
    # 1인 경우 종료
    if N == 1:
        return d[1]
    
    # 과거에 계산한 적이 있는 경우 종료
    if d[N]:
        return d[N]
   
    # 피보나치 수열 재귀
    # 0호출 횟수와 1호출 횟수도 더함
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

