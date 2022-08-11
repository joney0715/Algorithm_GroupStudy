N=int(input())
N_list=[]
s=1
while s*3!=N:
    s = s*3
    N_list.append(s)

s=[[1,1,1],[1,0,1],[1,1,1]]
def makelist(s,N):
    slist=[]
    for i in range(N):
        slist.append(s[i]*3)
    for i in range(N):
        slist.append(s[i]+[0]*N+s[i])
    for i in range(N):
        slist.append((s[i]*3))
    return(slist)
        

def star(lists,N):
    for i in range(N):
        for j in range(N):
            if lists[i][j]==1:
                print('*',end='')
            else:
                print(' ',end='')
        print()

for i in N_list:
    s=makelist(s,i)
star(s,N)