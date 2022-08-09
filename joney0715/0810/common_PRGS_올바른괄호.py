def solution(s):

    # 처음부터 닫는 괄호가 나오면
    # 틀린 경우이기 때문에 False
    if s[0] == ')':
        return False
    
    # 스택 정의
    stack = []
    # 괄호 하나씩 처리
    for char in s:
        # 여는 괄호인경우 스택에 추가
        if char == '(':
            stack.append(char)

        # 닫는 괄호인 경우 스택에서 최상위 데이터 제거
        elif char == ')' and len(stack):
            stack.pop()
        
        # 닫는 괄호가 나왔는데 스택이 비어있는 경우
        else:
            return False

    # 스택에 뭔가 남아있다면 괄호가 페어가 되지 않았다는 증거
    if len(stack) != 0:    
        return False
    else:
        return True