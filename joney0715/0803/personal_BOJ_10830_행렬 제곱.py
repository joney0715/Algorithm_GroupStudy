# 입력 값
N, B = map(int, input().split())
matrix = []
for _ in range(N):
    m = list(map(int, input().split()))
    matrix.append(m)

# 행렬의 곱
def multiple(matrix_a, matrix_b):
    # 곱 결과 초기화
    matrix_c = []

    # matrix_a의 행
    for a in range(N):
        # 계산 결과의 행 초기화
        result = []
        # matrix_b의 열
        for b in range(N):
            s = 0
            # matrix_a의 열, matrix_b의 행           
            for c in range(N):
                # 각 요소의 곱
                s += matrix_a[a][c] * matrix_b[c][b]
            # 1000으로 나눈 나머지 (문제의 요구사항)
            s = s % 1000
            #계산 결과의 행
            result.append(s)
        matrix_c.append(result)
    return matrix_c

# 행의 제곱 계산
def divide(matrix, B):
    # 지수가 1인 경우
    if B == 1:
        # 지수가 1인 경우도 1000으로 나눠야 하는거 주의
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] % 1000
        return matrix

    # 지수를 2로 나눠서 계산
    # A^(a+b) = A^a * A^b 의 원리
    a = divide(matrix, B//2)
    # 지수가 홀수인 경우
    # A^(2a +1) = A^a * A^a * A
    if B % 2:        
        matrix_c = multiple(a, a)
        matrix_c = multiple(matrix_c, matrix)
        return matrix_c
    # 짝수인 경우
    # A^(2a +1) = A^a * A^a
    else:
        matrix_c = multiple(a, a)
        return matrix_c
    
# 결과 출력
matrix_c = divide(matrix, B)
for row in matrix_c:
    print(*row) # 언패킹 응용