from itertools import combinations

# 괄호로 묶여있는 수식 입력
Input = list(input())

# 괄호를 짝짓기 위한 스택과
# 짝이 지어진 괄호를 넣기 위한 리스트 초기화
stack = []
pair = []

#입력한 수식을 문자열로써 하나씩 처리
for idx, char in enumerate(Input):

    # 여는 괄호인 경우 그 인덱스 스택에 추가   
    if char == '(':
        stack.append(idx)

    # 닫는 괄호인 경우 스택 최상단 값 빼기
    # 닫는 괄호의 인덱스와 함께 리스트에 추가
    if char == ')':
        pair.append([stack.pop(), idx])

# list가 아닌 set으로 한 이유
# list로 하면 ((1+2)) 같이 연속적인 괄호에서 오답처리
answer = set()

# 콤비네이션 모듈을 사용해서 제거할 수 있는 괄호의 경우의 수를 전부 계산
for i in range(1,len(pair)+1):

    # 괄호 1개만 없애는 경우 ~ 괄호 n개를 없애는 경우의 경우의 수를 계산
    for comb in list(combinations(pair, i)):

        # 입력된 수식 얕은 복사
        Input_c = Input[:]

        # 괄호가 들어간 부분은 비어있는 문자열로 치환
        for j, k in comb:
            Input_c[j] = ''
            Input_c[k] = ''

        #괄호가 없어진 수식 set에 추가
        answer.add(''.join(Input_c))

# 리스트로 바꾸고 사전순으로 정렬
answer = list(answer)
answer.sort()

# 정답 출력
for a in answer:
    print(a)
