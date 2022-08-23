T = int(input())

for tc in range(T):
    N = int(input())
    
    temp_list = [[1, 0], [0, 1]]
    
    if N <= 1:
        print(temp_list[N][0], temp_list[N][1])
        
    else:
        for i in range(2, N + 1):
            temp_list[0].append(temp_list[0][i - 1] + temp_list[0][i - 2])
            temp_list[1].append(temp_list[1][i - 1] + temp_list[1][i - 2])
            
        print(temp_list[0][N], temp_list[1][N])