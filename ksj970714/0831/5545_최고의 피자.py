N = int(input())
A,B = map(int,input().split())
C = int(input())
D = []
for i in range(N):
    D.append(int(input()))

D.sort(reverse=True)

kcal = C
won = A
fat = [C/A]
for toping in D:
    kcal += toping
    won += B
    fat.append(kcal/won)


print(int(max(fat)))