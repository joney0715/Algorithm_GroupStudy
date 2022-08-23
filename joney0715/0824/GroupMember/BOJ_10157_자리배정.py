C, R = map(int, input().split())

K = int(input())

seat = [[0]*C for _ in range(R)]

d_r = [1, 0, -1, 0]
d_c = [0, 1, 0, -1]

d = c = r = 0
k = 1
if K > C * R:
    print(0)
else:
    while k <= K: 
        seat[r][c] = k

        r_next = r + d_r[d]
        c_next = c + d_c[d]
        if r_next < 0 or r_next >= R or c_next < 0 or c_next >= C or seat[r_next][c_next]:
            d = (d+1) % 4
            r += d_r[d]
            c += d_c[d]

        else:
            r += d_r[d]
            c += d_c[d]

        k += 1

    print(c-d_c[d]+1, r-d_r[d]+1)
