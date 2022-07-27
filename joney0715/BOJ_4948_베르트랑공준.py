# 소수 카운팅 함수
def count_prime(N):
    count = 0
    # N과 2N 사이의 범위 
    for n in range(N+1, 2*N+1):
        if prime[n]:
            count += 1
    return count

# 제한 범위 내의 소수를 미리 계산해둠
n = 123456 * 2 + 1
prime = [True] * n
# 소수인지 판별할 숫자의 제곱근
# 제곱근이 대략 약수 중간이기 때문 
for i in range(2, int(n**0.5)+1):
    # 과거의 계산으로 i가 소수가 아니라면 처리하지 않음
    # i가 소수가 아니라면 i의 배수도 전부 소수가 아닌 상태
    if prime[i]:
        # 에라토스테네스 체로 소수 아닌 숫자 거르기
        # i의 배수를 전부 소수가 아닌 것으로 처리
        for j in range(2*i, n, i):
            prime[j] = False

# 테스트 데이터 입력
Num = []
while True:
    N = int(input())
    if N == 0:
        break
    Num.append(N)

# 연산
for N in Num:
    print(count_prime(N))
