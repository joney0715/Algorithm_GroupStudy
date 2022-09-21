T = 10


for test in range(T):
    S100 = int(input())
    temp_table = []
    table = []

    for i in range(100):
        temp_table.append(list(map(int,input().split())))

    for i in range(100):
        templist = []
        for j in range(100):
            templist.append(temp_table[j][i])
        table.append(templist)
    print(len(table),len(table[0]))
    #반전 완료
    gyochack = 0
    stack = []
    for line in table:
        stack = []
        for jasuck in line:
            if stack != [] and jasuck == 2:
                gyochack += 1
                stack = []
            elif jasuck == 1:
                stack.append(1)
    print('#{} {}'.format(test + 1, gyochack))