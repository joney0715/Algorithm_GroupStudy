N = int(input())
A = list(map(int,input().split()))
A.append(-1)
stack = []

for index in range(N):
    stack.append(index)
    for _ in range(len(stack)):
        if A[stack[-1]] < A[index+1]:
            A[stack.pop()] = A[index+1]
        else:
            break

#스택에서 못 빠진거 싹다 -1로 처리.
for index in stack:
    A[index] = -1

A.pop()

print(*A)