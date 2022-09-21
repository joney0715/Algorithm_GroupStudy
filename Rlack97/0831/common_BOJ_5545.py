N = int(input())
A, B = map(int,input().split())
C = int(input())
topping_cal = []

for i in range (N):
    D = int(input())
    topping_cal.append(D)
    # 입력값 받기

Bk = sorted(topping_cal,reverse=True)
# 역순으로 정렬 ( 1원당 칼로리 효율이 좋은 토핑 순서)

calories = C
price = A
max_value = C / A
# 값 변경을 위한 기본값 지정

for i in Bk:
    calories += i
    price += B
    # 가격과 칼로리를 하나씩 더해 줌

    if max_value < calories/price:
        max_value = calories/price
        # 더 좋은 값이 나온다면 갱신
    
    else :
        break
    # 그렇지 않다면 이미 효율은 계속 떨어질 수밖에 없으므로 브레이크


print(int(max_value))