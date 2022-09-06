
def dfs(r, c, cnt):
    if r < 0 or r >= N or c < 0 or c >= N:
        return False

    if mapping[r][c] == '1':
        mapping[r][c] = '0'
        visit[r][c] = cnt

        dfs(r+1, c, cnt)
        dfs(r-1, c, cnt)
        dfs(r, c+1, cnt)
        dfs(r, c-1, cnt)

        return True

    return False

N = int(input())

mapping = [list(input()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

answer = 0
cnt = 1
for row in range(N):
    for col in range(N):
        if mapping[row][col] and not visit[row][col]:
            if dfs(row, col, cnt):
                answer += 1
                cnt += 1

N_list = [0] * (cnt)
for i in range(1, cnt):
    for x in visit:
        N_list[i] += x.count(i)
    
print(answer)
N_list.sort()
for j in range(1, cnt):
    print(N_list[j])