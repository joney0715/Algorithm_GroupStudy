mapping = [[0]*100 for a in range(100)]
#100 x 100 배열 도화지

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for b in range (x1,x2):
        for a in range(y1,y2):    
            mapping[a][b] = 1  

Total = 0

for y in mapping:
    for x in y:
        if x == 1:
            Total += 1


print(Total)