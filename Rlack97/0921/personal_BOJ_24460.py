# 특별상이라도 받고 싶어 풀이
# 2022-09-16

N = int(input())
chiars = [list(map(int,input().split())) for _ in range(N)]
# 입력값

def special_prize(N, D_list):
    if N == 2 or N == 1:
        A = []
        for a in D_list:
            for i in range(N):
                A.append(a[i])
        A.sort()
        if len(A) != 1:
            return A[1]
        else:
            return A[0]
    # 재귀 종료 조건 : 다 나눠서 N이 2가 되거나, 처음부터 N이 1인 경우
    # 뒤에서 두번째 값을 반환
    
    else: 

        seperated_1 = [[0]*(N//2) for _ in range(N//2)]
        seperated_2 = [[0]*(N//2) for _ in range(N//2)]
        seperated_3 = [[0]*(N//2) for _ in range(N//2)]
        seperated_4 = [[0]*(N//2) for _ in range(N//2)]

        for a in range(N//2):
            for b in range(N//2):
                
                seperated_1[a][b] = D_list[a][b]
                seperated_2[a][b] = D_list[a+N//2][b]
                seperated_3[a][b] = D_list[a][b+N//2]
                seperated_4[a][b] = D_list[a+N//2][b+N//2]
                # 구역을 나눠서 따로 저장
        Q = []
        Q.append(special_prize(N//2, seperated_1))
        Q.append(special_prize(N//2, seperated_2))
        Q.append(special_prize(N//2, seperated_3))
        Q.append(special_prize(N//2, seperated_4))
        # 각 구역의 재귀값을 리스트에 저장

        Q.sort()

        return Q[1]
        # 리스트에서 두번째로 작은 값 반환

print(special_prize(N, chiars))
