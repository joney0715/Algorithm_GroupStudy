# 입력값
N, B = map(int, input().split())
matrix = []
for _ in range(N):
    m = list(map(int, input().split()))
    matrix.append(m)

#행렬의 곱
def multiple(matrix_a, matrix_b):
    # 계산 결과 초기화
    matrix_c = []

    # 곱 계산
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

# A^3 * A^3 = A^6 의 법칙을 이용해서
# 지수를 2로 나눠서 계산 횟수를 줄임
def divide(matrix, B):

    # 지수가 1인 경우
    if B == 1:
        # 1000으로 나눈 나머지를 구하기
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] % 1000
        return matrix

    # 지수가 홀수인 경우와 짝수인 경우로 나누기
    a = divide(matrix, B//2)

    # 지수가 홀수인 경우
    # A^5 = A^2 * A^2 * A
    if B % 2:        
        matrix_c = multiple(a, a)
        matrix_c = multiple(matrix_c, matrix)
        return matrix_c

    # 지수가 짝수인 경우
    else:
        matrix_c = multiple(a, a)
        return matrix_c

# 연산 및 출력 
matrix_c = divide(matrix, B)
for row in matrix_c:
    print(*row)