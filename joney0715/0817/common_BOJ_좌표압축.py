N = int(input())

X_list = list(map(int, input().split()))

# set을 사용해서 중복된 요소 제거 후 정렬
X_sort = sorted(set(X_list))

# dict을 사용해서 각 요소보다 작은 값의 수를 저장
# 키 : 요소, 값 : 작은 값의 수
answer = dict()
for i in range(len(X_sort)):
    answer[X_sort[i]] = i

for j in range(N):
    print(answer.get(X_list[j]), end=' ')