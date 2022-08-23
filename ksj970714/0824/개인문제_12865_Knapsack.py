N, K = map(int,input().split())
a = [0]*(K+1)

knapsack = [] #얕은복사방지
for _ in range(N+1):
    knapsack.append(a[:])

val = [0]
weight = [0]
for case in range(N):
    a, b = map(int,input().split())
    if K > a:
        weight.append(a)
        val.append(b)
print(weight)
print(val)
for i in range(1,N+1): #1번부터 N+1번까지 순회
    print('N',i)
    w = weight[i]
    v = val[i]
    print(w,v)
    print(i)
    print(knapsack[i])
    for idx in range(w,K+1):
        print(idx,"idx",)

        if knapsack[i-1][idx] < knapsack[i-1][idx+1-w]+v:
            knapsack[i][idx] = knapsack[i-1][idx+1-w]+v
        else:
            knapsack[i][idx] = knapsack[i-1][idx]

print(knapsack)
