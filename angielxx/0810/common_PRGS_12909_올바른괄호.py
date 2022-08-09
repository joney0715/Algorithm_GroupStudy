def solution(s):
    stack = []
    for i in range(len(s)):
        stack.append(s[i])
        if s[i : i+2] == '()':
            stack.pop()
            stack.pop()

print(solution('()()'))
print(solution('(())()'))
print(solution(')()('))
print(solution('(()('))