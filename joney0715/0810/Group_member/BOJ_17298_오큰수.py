import sys
# 수열 크기
N = int(sys.stdin.readline())
# 
A = list(map(int, sys.stdin.readline().split()))

# 기본값을 -1로 리스트 생성
answer = [-1] * N
#스택 정의
stack = []

# 수열 하나씩
for i in range(N):
    # 스택에 요소가 들어있으며
    # 스택 최상단값이 해당 수열의 값보다 작은 경우
    while stack and A[stack[-1]] < A[i]:
        # 스택에서 뺀 뒤 answer리스트 갱신
        a = stack.pop()
        answer[a] = A[i]
    stack.append(i)
print(*answer)

"""
로직을 정말 이해하기 힘든 문제

임의의 수열 값A[i]에서 스텍의 값(과거의 수열 값 A[i-1], A[i-2].....) 과 비교해서 A[i]이 크다면
과거의 수열들의 NGE값은 자연스럽게 A[i]이 됨

수열 값 A[i]의 인덱스i 스택에 추가
"""