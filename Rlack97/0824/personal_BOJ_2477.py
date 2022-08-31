K = int(input())

mapping = [[] for _ in range(5)]


for _ in range(6):
    a, b = map(int,input().split())
    mapping[a].append(b)

mapping2 = [0]*4
mapping2[1] = mapping[1]
mapping2[3] = mapping[2]
mapping2[0] = mapping[3]
mapping2[2] = mapping[4]

# 북 동 남 서 순으로 변경. 
# 순서대로 저장했을 때, len이 1인 경우를 제하면 시계방향으로 순회할 경우,
# 첫 변의 두번째 값과 두번째 변의 첫번째 변을 곱하면 작은 사각형
# 너무 무식하게 품

total = []
minus = []


for m in mapping2:
    if len(m) == 1:
        total.append(m)
    elif len(m) == 2:
        minus.append(m)
        # 길이가 2인 리스트는 작은 사각형이 들어가있는 곳.

        
print(total)
print(minus)

total_squre = total[0][0] * total[1][0]
# 전체 넓이는 길이가 1개인 리스트끼리의 곱

minus_squre = minus[0][1] * minus[1][0]


print((total_squre-minus_squre)*K)