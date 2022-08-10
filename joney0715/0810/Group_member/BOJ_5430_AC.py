T = int(input())

for _ in range(T):
    # 함수 입력
    F = input()
    # 숫자의 개수 
    N = int(input())
    # 리스트를 문자열로 입력
    numbers = input()
    # 리스트 형태로 된 문자열을 리스트로 변경
    numbers = numbers[1:-1].split(',')
    
    # N이 0이라면 비어있는 리스트를 정의
    # 이 연산을 하지 않으면 numbers = input()로 []를 입력 받았을때
    # numbers = numbers[1:-1].split(',')의 연산 결과가 ['']가 되어서
    # 비어있는 리스트가 아닌 비어있는 문자열이 있는 리스트가 됨
    if not N:
        numbers = []

    # R이 나올때마다 reverse를 하면 타임아웃
    # R이 홀수일 때면 마지막 한번만
    # 짝수면 reverse를 하지 않는 방법 채용
    R = 0
    # 함수 하나씩 처리
    for f in F:
        # R이 나오면 R의 개수를 하나씩 늘림
        if f == 'R':
            R += 1
        # D가 나오면 삭제 작업 수행
        else:
            # 리스트가 비어있으면 error를 출력하고 break
            if not len(numbers):
                print('error')
                break
            
            # 리스트에 요소가 있는 경우
            else:
                # 앞에 나온 R의 개수가 짝수라면
                # 리스트가 원래 상태이기 때문에
                # 리스트 첫 번째 요소 하나 제거
                if not R % 2:
                    numbers.pop(0)

                # 앞에 나온 R의 개수가 홀수라면
                # 리스트가 거꾸로 되어있기 때문에
                # 리스트 가장 뒤 요소 하나 제거
                else:
                    numbers.pop()

    # for-else 문을 사용해서 반복문이 break하지 않는다면
    # 아래의 연산 처리
    else:
        # R이 홀수일 때 reverse를 한번만 하고 출력
        if R % 2: 
            numbers.reverse()
            print('['+','.join(numbers)+']')

        # R이 짝수일 때는 그냥 출력
        else:
            print('['+','.join(numbers)+']')

'''
아래 코드는 틀린 코드
아래 코드가 안되는 반례
1
D
1
[1]
답: []
출력: error

경계값을 조심하자
'''
'''
T = int(input())

for _ in range(T):
    F = input()
    N = int(input())
    numbers = input()
    numbers = numbers[1:-1].split(',')
    
    if not N:
        numbers = []
    R = 0
    for f in F:
        if f == 'R':
            R += 1
        else:
            if not len(numbers):
                break
            
            else:
                if R % 2:
                    numbers.pop()
                else:
                    numbers.pop(0)

    if len(numbers):
        if R % 2:
            numbers.reverse()
            print('['+','.join(numbers)+']')
        else:
            print('['+','.join(numbers)+']')
    else:
        print('error')
'''
