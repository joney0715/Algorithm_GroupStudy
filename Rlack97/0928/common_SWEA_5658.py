# 5658_보물상자비밀번호  풀이
# 2022-09-24

sixteen = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
    'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

def st_to_ten(num):
    N = len(num)
    total = 0
    for i in range(N):
        total += sixteen[num[i]] * (16**(N-i-1))
    return total

T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    stlist = list(input())
    possible_num = set()

    for a in range(N//4):
        com1 = "".join(stlist[:N//4])
        com2 = "".join(stlist[N//4:N//2])
        com3 = "".join(stlist[N//2:(N//4)*3])
        com4 = "".join(stlist[(N//4)*3:])

        possible_num.add(com1)
        possible_num.add(com2)
        possible_num.add(com3)
        possible_num.add(com4)
        stlist.insert(0,stlist.pop(-1))
        #금단의 insert 0... 과연
    
    ten_num = []
    for p in possible_num:
        ten_num.append(st_to_ten(p))

    ten_num.sort(reverse=True)
    
    answer = ten_num[K-1]
    print('#{} {}'.format(tc,answer))