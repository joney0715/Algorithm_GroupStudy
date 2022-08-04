# ★ > ● > ▲ > ■ 순으로 강하다.

#N은 총 라운드 수.
#그 다음 줄은 각각 그림의 총 갯수.
#그 다음은 A가 낸 그림. 
#그 다음은 B가 낸 그림
#출력은 라운드의 승자. 무승부는 D


def winner(a,b,c):
    A = a.count(c)
    B = b.count(c)
    if c == 0:
        return 'D'
    elif A > B:
        return 'A'
    elif A < B:
        return 'B'
    else:
        return winner (a,b,c-1)                

N = int(input())

Result = []

for a in range(N):
    A = list(map(int,input().split())) 
    B = list(map(int,input().split()))
    del A[0]
    del B[0]
    Result.append(winner(A,B,4))

for T in Result:
    print(T)
    
