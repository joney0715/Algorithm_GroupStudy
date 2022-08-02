from itertools import combinations

Input = list(input())

stack = []
pair = []
for idx, char in enumerate(Input):   
    if char == '(':
        stack.append(idx)
    if char == ')':
        pair.append([stack.pop(), idx])

answer = set()
for i in range(1,len(pair)+1):
    for comb in list(combinations(pair, i)):
        Input_c = Input[:]
        for j, k in comb:
            Input_c[j] = ''
            Input_c[k] = ''
        answer.add(''.join(Input_c))

answer = list(answer)
answer.sort()
for a in answer:
    print(a)
