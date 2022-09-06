# combi 함수 선언
answer = []
def combi(i, list):
    for n in range(i, len(num_list)):
        combi(n + 1, list + [num_list[n]])
    answer.append(list)

# 입력값 받기
N = int(input())
K = int(input())
num_list = []
for num in range(1, N + 1):
    num_list.append(num)
    
combi(0, [])

# 부분집합 중 길이가 K인 부분집합 출력
for subset in answer:
    if len(subset) == K:
        print(subset)