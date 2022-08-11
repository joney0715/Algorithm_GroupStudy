dec = []

N = int(input())

for i in range(N):
    name = str(input())
    need_candy,total_candy = map(int,(input()).split())
    dec.append({'name' : name, 'need_candy' : need_candy, 'total_candy':total_candy})
#입력값을 dict들의 list로 정리하여 받습니다.

total_evolve = 0
for k in dec:
    able_ev = 0
    while k['total_candy'] - k['need_candy'] >= 0:
        able_ev += 1
        k['total_candy'] -= k['need_candy'] - 2
    k.update({'ev_time' : able_ev})
    total_evolve += able_ev
# 각 dict마다 진화 가능 횟수를 카운트합니다.

dec.sort(key = lambda x : x['ev_time'],reverse=True)
# 진화 가능 횟수를 키로 하여 dict를 정렬합니다.

print(total_evolve)
print(dec[0]['name'])
# 총 진화 횟수 및 가장 진화 횟수가 많은 포켓몬의 이름을 출력합니다.