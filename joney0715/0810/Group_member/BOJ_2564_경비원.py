# 입력된 동근이의 위치, 가게 위치를 
# 데카르트 좌표로 바꾸는 함수 
def coordinate(d,p):
    if d == 1:
        return p,hight
    elif d == 2:
        return p,0
    elif d ==3:
        return 0,hight-p
    else:
        return width,hight-p

# 좌표계(담당하고 있는 직사각형) 입력
width, hight = map(int, input().split())
# 가게 수
store = int(input())

# 가게 위치를 입력
stores = []
for _ in range(store):
    d, p = map(int, input().split())
    stores.append(coordinate(d,p))

# 동근이 위치 입력
position = tuple(map(int, input().split()))
position = coordinate(position[0], position[1])

# 반복문으로 가게를 하나씩 처리
answer = 0
for store in stores:
    # 동근이 위치와 가게 위치의 상대 좌표 계산
    x = abs(position[0] - store[0])
    y = abs(position[1] - store[1])

    # 동근이가 서쪽 혹은 동쪽에 위치해 있고
    # 가게가 맞은 편에 있는 경우
    if x == width:
        a = min(position[1]+width+store[1], 2*hight-(position[1]+store[1])+width)
        answer += a
    
    # 동근이가 북쪽 혹은 남쪽에 위치해 있고
    # 가게가 맞은 편에 있는 경우
    elif y == hight:
        a = min(position[0]+hight+store[0], 2*width-(position[0]+store[0])+hight)
        answer += a

    # 동근이의 위치와 가게 위치가 직교한는 축에 있는 경우
    else:
        a = x+y
        answer += a

print(answer)