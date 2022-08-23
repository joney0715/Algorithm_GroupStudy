
def check(road):
    cnt = 1
    flag = 0
    # 맨 앞 요소는 빼고 시작
    for i in range(1,N):    
        # 앞 요소와 같은 경우
        if road[i] == road[i-1]:
            cnt += 1
            # flag가 1인 경우
            if flag:
                if cnt == x:
                    flag = 0
                    cnt = 0
            # flag가 0인 경우
            else:
                pass
        
        # 앞 요소와 다른 경우
        else:
            # 앞 요소랑 1차이가 넘는 경우
            if abs(road[i] - road[i-1]) > 1:
                return False

            # 요소와의 차이가 1인 경우
            else:
                # 앞 요소가 더 큰 경우
                if road[i] < road[i-1]:
                    # flag가 1인 경우
                    if flag:
                        return False
                    
                    # flag가 0인 경우
                    else:
                        flag = 1
                        cnt = 1
                
                # 앞 요소가 더 작은 경우
                else:
                    # 앞에 있는 고지대가 처리가 안된 경우
                    if flag:
                        return False
                    # 경사로를 짓기에 땅이 부족한 경우
                    elif cnt < x:
                        return False
                    # 경사로를 지을 수 있는 경우
                    else:
                        cnt = 1
    
    if flag:
        return False
    else: 
        return True


T = int(input())

for tc in range(1, T+1):
    N, x = map(int, input().split())

    map_list = [list(map(int, input().split())) for _ in range(N)]

    airstrip = 0
    for r in range(N):
        if check(map_list[r]):
            airstrip += 1

    for c in range(N):
        col = []
        for r in range(N):
            col.append(map_list[r][c])
        if check(col):
            airstrip += 1

    print('#{}'.format(tc), airstrip)

                

                