max = 123456

A = [1]*(max*2+1)

A[0] = 0
A[1] = 0

for i in range(2,len(A)//2):
    for j in range(i + i, len(A), i):
        A[j] = 0

T = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        T.append(sum(A[n+1:2*n+1]))

for k in range(len(T)):
    print(T[k])