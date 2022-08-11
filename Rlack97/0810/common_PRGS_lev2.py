s = list(input())              
len = 0

for w in s:
    len += 1

# 리스트의 길이를 측정

cnt = 0
for i in range(len):                   # 인덱스 값을 기준으로 접근
    if s[i] == '(':                    # 괄호가 열렸을 때,
        for k in range(i,len):         
            if s[k] == ')' and s[i] != 0: 
                # 그 뒤에 있는 닫힌 괄호를 찾음. 이미 0처리된 괄호랑 중복 방지
                s[i] = 0                  
                s[k] = 0
                cnt += 1                # 처리한 값을 0으로 변환하고 카운트 +1
                

if cnt*2 == len:                        # 카운트한 쌍이 전체 길이의 절반이면 올바른 괄호
    print(True)
else:
    print(False)                        # 그렇지 않으면 올바르지 못한 괄호
        
        