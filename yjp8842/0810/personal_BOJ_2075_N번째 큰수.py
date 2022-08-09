# 버블 정렬 함수 정의하기
def bubble_sort(a, N):
    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                
N = int(input())
num_list = []
# 2차원 리스트 input 받기
for i in range(N):
    input_list = list(map(int, input().split()))
    num_list.append(input_list)

# 2차원 리스트를 1차원 리스트로 변환하기
result_list = []
for inner_list in num_list:
    for data in inner_list:
        result_list.append(data)

        # 오름차순으로 정렬
        M = len(result_list)
        for i in result_list:
            bubble_sort(result_list, M)

# 마지막에서 N번째 값    
print(result_list[M - N])