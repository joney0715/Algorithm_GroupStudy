# 다오와 트리플 멕스 게임 풀이
# 2022-09-01

N = int(input())
A_list = list(map(int,input().split()))

# subsequence = 기존 배열에서 0개 이상의 원소를 제거한 배열, 빈 배열 제외
# subarray = 주어진 배열의 연속된 부분
# mex = 배열에서 나타나지 않는 0 이상의 가장 작은 정수.

A_list.sort()

if A_list[0] != 0:
    print(0)
# 배열에 0이 없는 경우, 무조건 0이 나옴

elif sum(A_list)==0:
    print(1)
# 배열에 0만 있는 경우, 무조건 1이 나옴 
# 0 -> 1 -> 0 -> 1

else:
    for a in range(N):
        if a == N-1:
            answer = A_list[a] + 3
            print(answer)
            break
        # 연속되는 수가 마지막까지 이어질 경우를 잡아주는 if

        elif A_list[a] == A_list[a+1] or A_list[a] == A_list[a+1] -1 :
            pass
        # 중복되거나 연속되는 수일 경우 mex값에 영향을 주지 않음.

        else:
            answer = A_list[a] + 3
            print(answer)
            break
        # 값이 연속되지 않는 시점에서 다음 리스트의 mex값이 정해짐. 
        # 이를 두번 반복하므로 값이 +3