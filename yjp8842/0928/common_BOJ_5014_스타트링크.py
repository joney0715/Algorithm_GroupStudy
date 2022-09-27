# 답은 나오는데.. 틀림.. ㅠ

F, S, G, U, D = map(int, input().split())

visit = [0] * (F + 1)
visit[S] = 1
lst = [[S, 0]]
flag = -1

while lst:
    # 현재 위치, 버튼 누른 횟수
    current_d, cnt = lst.pop()
    # print(current_d, cnt)
    
    # 만약 현재 위치가 스타트링크가 위치한 층이라면 break
    if current_d == G:
        flag = cnt
        break
    
    if (current_d > G and D == 0) or (current_d < G and U == 0):
        break
    
    if current_d + U <= F:
        if visit[current_d + U] == 0:
            visit[current_d + U] = 1
            lst.append([current_d + U, cnt + 1])
            
    if current_d - D > 0:
        if visit[current_d - D] == 0:
            visit[current_d - D] = 1
            lst.append([current_d - D, cnt + 1])
            
if flag == -1:
    print("use the stairs")
else:
    print(flag)