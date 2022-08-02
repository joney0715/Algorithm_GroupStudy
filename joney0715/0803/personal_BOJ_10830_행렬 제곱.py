N, B = map(int, input().split())
matrix = []
for _ in range(N):
    m = list(map(int, input().split()))
    matrix.append(m)

def multiple(matrix_a, matrix_b):
    matrix_c = []
    for a in range(N):
        result = []
        for b in range(N):
            s = 0           
            for c in range(N):
                s += matrix_a[a][c] * matrix_b[c][b]
            s = s % 1000
            result.append(s)
        matrix_c.append(result)
    return matrix_c

def divide(matrix, B):
    if B == 1:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] % 1000
        return matrix

    a = divide(matrix, B//2)
    if B % 2:        
        matrix_c = multiple(a, a)
        matrix_c = multiple(matrix_c, matrix)
        return matrix_c

    else:
        matrix_c = multiple(a, a)
        return matrix_c
    
matrix_c = divide(matrix, B)
for row in matrix_c:
    print(*row)