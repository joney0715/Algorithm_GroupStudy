'''
먼저 n<=123456이고, 최대로 조사해야 하는것이 2n까지이므로,
2*123456까지 소수인지 판별할 수 있다면 이 문제는 해결된다.
그러나 자연수 n이 소수인지 판별할때 흔히 쓰는 방법인,
n의 제곱근 미만의 수로 다 나눠보는 방법은 시간초과가 뜬다.
(4, 6등 소수가 아닌 수로도 나누게됨)

따라서 이를 해결하기 위해 500까지의 소수를 미리 리스트로 구해놓고 활용
123456*2는 500의 제곱(250000)보다 작으니까.
'''

prime_number = [2]
prime = []
for i in range(3,500):
    for j in range(len(prime_number)):
        if i % prime_number[j] == 0:
            break
    else: 
        prime_number.append(i)        
'''
앞서 언급한 2~500 사이의 소수를 구하는 과정
리스트에 2를 넣고 시작(리스트에 아무것도 안 넣으면 인덱스에러가 났던것 같음) 
i보다 작은 어떤 소수로도 나누어떨어지지 않으면
(즉, i가 소수로 판별되면) 리스트에 집어넣음. 
따라서 prime_number에는 500보다 작은 소수만 들어있게 됨
'''     
for i in range(500,123456*2):
    for j in range(len(prime_number)):
        if i % prime_number[j] == 0:
            break
    else: 
        prime.append(i)
prime.extend(prime_number) 
#500이상의 소수만 있는 prime에 500이하의 소수가 들어있는 prime_number 추가.
'''
prime_number로 500~123456*2 범위 안의 수를 나눠보며 소수를 판별함.
'''

while True:        
    N = int(input())
    if N == 0 :
        break
    count = 0
    for i in prime:
        if N < i <= 2*N :
            count += 1
        
    print(count)

'''
N을 입력받아, prime에 속하는 원소가 N과 2N사이의 범위에 있다면
카운트+1을 해줌으로서 구간 사이의 소수의 수를 구한다.
'''