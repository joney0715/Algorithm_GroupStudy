dec = []

N = int(input())

for i in range(N):
    name = str(input())
    need_candy,total_candy = map(int,(input()).split())
    dec.append({'name' : name, 'need_candy' : need_candy, 'total_candy':total_candy})


total_evolve = 0
for k in dec:
    able_ev = 0
    while k['total_candy'] - k['need_candy'] >= 0:
        able_ev += 1
        k['total_candy'] -= k['need_candy'] - 2
    k.update({'ev_time' : able_ev})
    total_evolve += able_ev

dec.sort(key = lambda x : x['ev_time'],reverse=True)

print(total_evolve)
print(dec[0]['name'])

