C, R = map(int, input().split())
seat_list = [[0] * C for _ in range(R)]
K = int(input())

for i in range(R + 1):
    seat_list[i][C] = -1
    
for j in range(C + 1):
    seat_list[R][j] = -1
    
n = 0
m = 0
seat_list[0][0] = 1
