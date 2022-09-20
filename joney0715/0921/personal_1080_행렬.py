
def reverse(row, col):
    for r in range(row, row+3):
        for c in range(col, col+3):
            if A_matrix[r][c]:
                A_matrix[r][c] = 0
            else:
                A_matrix[r][c] = 1


N, M = map(int, input().split())

A_matrix = []
for _ in range(N):
    row = list(input())
    row = [int(i) for i in row]
    A_matrix.append(row)

B_matrix = []
for _ in range(N):
    row = list(input())
    row = [int(i) for i in row]
    B_matrix.append(row)

answer = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A_matrix[i][j] != B_matrix[i][j]:
            reverse(i, j)
            answer += 1

        if A_matrix == B_matrix:
            break
    if A_matrix == B_matrix:
        break

if A_matrix != B_matrix:
    print(-1)
else:
    print(answer)