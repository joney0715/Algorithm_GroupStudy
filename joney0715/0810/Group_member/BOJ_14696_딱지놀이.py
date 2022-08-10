T = int(input())

for _ in range(T):
    # 카드 정보 입력
    # 첫번째에 주어지는 카드 수는 필요없는 데이터이기 때문에 없앰
    A = list(map(int, input().split()))[1:]
    B = list(map(int, input().split()))[1:]

    # 카드 정렬
    A.sort()
    B.sort()

    # 둘중에 한 명이라도 카드가 없어질 때까지 반복
    while len(A) and len(B):
        # 가지고 있는 카드 중 가장 큰 카드
        a = A.pop()
        b = B.pop()

        # 같은 카드인 경우
        if a == b:
            # 둘다 다음에 꺼낼 카드가 없는 경우 비김
            if not len(A) and not len(B):
                print('D')
                break
            # A의 카드가 다 떨어진 경우
            elif not len(A) and len(B):
                print('B')
                break
            # B의 카드가 다 떨어진 경우
            elif len(A) and not len(B):
                print('A')
                break
            else:
                pass

        # 다른 카드인 경우
        else:
            # A가 크면 A승리
            if a > b:
                print('A')
                break
            # B가 크면 B 승리
            elif a < b:
                print('B')
                break
                    


