from itertools import combinations

Input = list(input())

# 괄호 페어를 확인 하기 위한 스택
stack = []
# 괄호가 있는 인덱스를 저장하기 위한 리스트
pair = []
for idx, char in enumerate(Input):   
    # 괄호가 열리면 스택에 추가
    if char == '(':
        stack.append(idx)
    # 괄호가 닫히면 스택에서 빼면서
    # 인덱스 정보 저장
    if char == ')':
        pair.append([stack.pop(), idx])

# 결과를 셋으로 하는 이유
# 리스트로 하면 ((1+2)) 같은 경우에 계산 안됨
answer = set()
for i in range(1,len(pair)+1):
    # 없애려는 괄호의 조합 계산
    for comb in list(combinations(pair, i)):
        # 원본 수식의 얕은 복사
        Input_c = Input[:]
        # 괄호가 있는 경우 빈 문자열로 바꾸기
        for j, k in comb:
            Input_c[j] = ''
            Input_c[k] = ''
        answer.add(''.join(Input_c))
        
# 리스트로 변환
answer = list(answer)
# 사전순으로 정렬 (문제의 요구사항)
answer.sort()
for a in answer:
    print(a)
