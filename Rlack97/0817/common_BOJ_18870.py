N = int(input())
Xs = list(map(int,input().split()))
result = []
# 값 입력

# 좌표 압축 = 원본이 되는 좌표값보다 작은, 중복되지 않는 좌표의 수

Ss = set(Xs)
# 중복값 제거를 위해 리스트를 세트로 변경

for a in Xs:
    cnt = 0
    # 기존 리스트의 요소들에 접근 
    # 세트에 접근하면, 중복 좌표들에 대한 출력 자체가 불가능해져서 안됨

    for k in Ss:
        # 세트에 접근해서,

        if k < a:
            cnt +=1
            # '리스트의 요소보다 작은' '세트 요소(중복되지 않는 좌표)'의 수를 계산

    result.append(cnt)
 
print (*result)