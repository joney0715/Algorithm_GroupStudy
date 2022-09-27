# 꿀 따기 게임 풀이
# 2022-09-16

N = int(input())
honey = list(map(int,input().split()))
honey_max = []

# 벌 - 벌 - 벌통
bee1 = sum(honey)-honey[0]
bee2_list = []
for i in range(1,N-1):
    bee2 = sum(honey[i+1:N]) - honey[i]
    bee2_list.append(bee2)
honey_max.append(bee1 + max(bee2_list))
    
# 벌통 - 벌 - 벌
bee2 = sum(honey)-honey[-1]
bee1_list = []
for i in range(1,N-1):
    bee1 = sum(honey[0:i]) - honey[i]
    bee1_list.append(bee1)
honey_max.append(max(bee1_list)+bee2)

# 벌 - 벌통 - 벌
thrd_list = []
for i in range(1,N-1):
    bee1 = sum(honey[1:i+1])
    bee2 = sum(honey[i:N-1])
    thrd_list.append(bee1+bee2)
honey_max.append(max(thrd_list))


print(max(honey_max))


# 일일히 더해서 해서 그렇고,
# 구간합을 미리 구해서 하면 100점이 나온다더라...