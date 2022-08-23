N = int(input())

# 타일이 1하나인 경우
if N == 1:
    print(1)
else:
    d = [0] * (N+1)
    d[1] = 1
    d[2] = 2

    # 계산 결과 리스트에 저장
    for i in range(3, N+1):
        d[i] = (d[i-1] + d[i-2]) % 15746

    # 마지막 요소 출력
    print(d[N])