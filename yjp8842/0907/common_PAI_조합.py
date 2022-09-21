""" # 나의 풀이
# 입력값 받기
N = int(input())
K = int(input())
num_list = []
for num in range(1, N + 1):
    num_list.append(num)

# combi 함수
answer = []
def combi(i, list):
    
    for n in range(i, len(num_list)):
        combi(n + 1, list + [num_list[n]])
    
    # 결과를 매번 추가
    answer.append(list)
    
combi(0, [])

# 부분집합 중 길이가 K인 부분집합 출력
for subset in answer:
    if len(subset) == K:
        print(subset) """






# 교재 풀이
def combine(self, n, k):
    results = []

    def dfs(elements, start, k):
        # k가 0이 되면 결과에 추가
        if k == 0:
            results.append(elements[:])
            return

        # 자신 이전의 모든 값을 고정하여 재귀 호출
        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    return results

n = int(input())
k = int(input())

print(combine([], n, k))