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

total = []
minus = []
for m in mapping2:
    if len(m) == 1:
        total.append(m)
    elif len(m) == 2:
        minus.append(m)

total_squre = total[0][0] * total[1][0]
minus_squre = minus[0][1] * minus[1][0]

print((total_squre-minus_squre)*K)