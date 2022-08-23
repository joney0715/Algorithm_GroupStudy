import sys
N, M = map(int,input().split())
if N == 1:
    print(N)
    quit()
line = {}

spot = [0]*(N+1)
stack = []
temp = {}
for i in range(1,N+1):
    temp[i] = 0
for i in range(1,N+1):
    line[i] = []
count = N
solve = []

for i in range(M):
    a, b = (map(int,sys.stdin.readline().split()))
    temp[b] += 1 #진입 차수
    line[a].append(b)  #방향


for push in range(1,len(temp)+1): #stack에 추가
    if temp[push] == 0 :
        stack.append(push)

stack_temp=[]
while count > 0:
    for i in range(len(stack)):
        num = stack.pop()

        for dim in line[num]: #dim: line에 들어있던 해당 노드로부터 시작된 간선의 종착지
            temp[dim] -= 1 #간선 제거
            if temp[dim] == 0:
                stack_temp.append(dim)
        temp[num] = 1
        solve.append(num)  # 이후 정렬 리스트에 num 추가
        count -= 1

    stack.extend(stack_temp)
    stack_temp=[]


          #중복 연산 방지를 위해 자신으로 향하는 간선 집어넣음(0이 아니라 연산안됨)



print(*solve)

