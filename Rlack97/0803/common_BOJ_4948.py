max = 123456

A = [1]*(max*2+1)  # 최대치까지 리스트 생성

A[0] = 0
A[1] = 0            # 1과 0은 소수가 아님


for i in range(2,len(A)//2):              # 원래는 루트 2까지의 약수만을 카운팅하지만, 에러가 나서 반값까지만 계산. 아마 0.5를 1/2로 해서 그런듯 합니다
    for j in range(i + i, len(A), i):     # 2i~A까지의 수들 중, 차잇값이 i인 (배수가 i인) 수들은 소수가 아님
        A[j] = 0                          # 해당 수들을 0으로 변환
              
T = []
while True:
    n = int(input())
    if n == 0:
        break         # 입력값이 0이면 브레이크
    else:
        T.append(sum(A[n+1:2*n+1]))    
                      # 공준 범위 내부의 1을 합(소수 갯수)를 리스트에 저장

for k in range(len(T)):
    print(T[k])       # 각 결과값을 줄을 나누어 출력