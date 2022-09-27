import sys
sys.stdin = open('sample_input.txt', 'r')

dct = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(input())
    pwd = []

    # N // 4만큼 회전
    for _ in range(N // 4):
        # 동일한 개수만큼 새로운 리스트에 append
        for i in range(N // (N // 4)):
            pwd.append(arr[i * (N // 4):i * (N // 4) + (N // 4)])
        # 마지막 값 pop해서 맨처음 인덱스 값으로 삽입 (회전)
        m = arr.pop()
        arr.insert(0, m)

    # 중복되는 값을 없애기 위한 작업
    lst = []
    for i in range(len(pwd)):
        if pwd[i] not in lst:
            lst.append(pwd[i])

    # 생성가능한 수를 내림차순으로 정렬
    new_pwd = sorted(lst, reverse=True)
    
    # K번째로 큰 수 (인덱스 값이므로 -1)
    result = new_pwd[K - 1]     

    # 16진수를 10진수로 변환하기
    cnt = 0
    for i in range(len(result)):
        # 만약 A ~ F에 해당하는 값이 나오면
        if result[i] in dct:
            cnt += int(dct[result[i]]) * (16 ** (len(result) - 1 - i))
        # 0 ~ 9에 해당하는 값이 나오면
        else:
            cnt += int(result[i]) * (16 ** (len(result) - 1 - i))

    print('#{} {}'.format(tc, cnt))