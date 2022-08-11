# BOJ 4948 베르트랑 공준 (실버2)

# 100000의 제곱근까지의 소수 리스트를 미리 만들어놓는다
# n ~ 2n 범위의 소수의 개수를 센다

all = range(1,123456*2) # 100000까지만 생각하고, 요구한 범위대로 안하니까 오답..
prime_numbers = list()
for i in all: # 오답! = 반복문, range를 줄이니까 답이 금방나옴
    for j in range(2, int(i**(1/2)) + 1):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    else:
        cnt = 0
        for i in prime_numbers:
            if n < i <= 2*n:
                cnt += 1
    print(cnt)