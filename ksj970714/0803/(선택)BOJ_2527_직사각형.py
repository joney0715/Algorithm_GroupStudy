answer = []
for i in range(4):
    
    temp_list = list(map(int,input().split()))
    ax = [temp_list[0],temp_list[2]]
    ay = [temp_list[1],temp_list[3]]
    bx = [temp_list[4],temp_list[6]]
    by = [temp_list[5],temp_list[7]]
    '''
    입력을 살짝 이상하게 했는데 그냥 ax[0],ax[1]= map(int,input())..
    식으로 받아도 무방했을 것 같다.
    ax에 들어가있는 것은 a의 X 좌표 2개(오른쪽이 왼쪽보다 큼). 
    ay에 들어가있는 것은 a의 y좌표 2개...
    '''

    '''
    두 사각형의 관계를 어떻게 꼭지점의 위치를 통해 설명할 수 있을 것인가?
    가 이 문제에서 던지는 질문인데,

    a의 X좌표 두개를 이은 선분, Y좌표 2개를 이은 선분이 있다고 가정하자.
    예를 들어 a의 X좌표 두 개가 (3,5), b의 X좌표가 (5,7)이라면
    "X좌표로만 보면" 둘은 한 점에서 만난다. 이때 x_status를 "point"라고 한다.

    (3,5) (4,6)일 경우는 (5,6)구간이 겹친다. 이때는 "line"이라고 한다.
    아예 (3,5) (6,7)처럼 구간이 만나지 않을때는 "none"이라고 한다.

    이때, x_status가 "point" 이고 y_status도 "point"라면 두 사각형은 한 점에서 만난다.
    위에서 든 예시를 그대로 이어보면, a의 x좌표가 (3,5) b의 x좌표가 (5,7)인데
    a의 y좌표가 (6,8), b의 y좌표가 (8,10)일 경우, 두 사각형은 (5,8)이라는 한 점에서 만나게 된다. 

    마찬가지로 x_status가 point이고 y_Status가 line일경우, 두 사각형은 서로 한 선에서 만난다.
    둘 다 line일 경우, 두 사각형은 범위를 공유한다.

    둘다 none일 경우, 두 사각형은 만나지 않는다.
    이러한 아이디어를 알고리즘으로 구현하였다.
    '''
                         
    if ax[0] == bx[1] or ax[1] == bx[0]:
        x_status = 'point'
                         
    elif ax[0] > bx[1] or ax[1] < bx[0]:
        x_status = 'none'
                         
    else:
        x_status = 'line'
    
    if ay[0] == by[1] or ay[1] == by[0]:
        y_status = 'point'
                         
    elif ay[0] > by[1] or ay[1] < by[0]:
        y_status = 'none'
                         
    else:
        y_status = 'line'
    
    if x_status == 'line' and y_status == 'line':
        answer.append('a')
    elif (x_status == 'line' and y_status == 'point') or (y_status == 'line' and x_status == 'point'):  
        answer.append('b')
    elif x_status == 'point' and y_status == 'point':
        answer.append('c')
    else: 
        answer.append('d')
for i in answer:
    print(i)