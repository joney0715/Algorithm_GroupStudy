import sys

sys.stdin = open('input_1220.txt', 'r')

for tc in range(1, 11):
    N = int(sys.stdin.readline())

    mag = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    answer = 0
    stack = []
    for i in range(N):
        for j in range(N):
            if mag[j][i] == 1:
                stack.append(mag[j][i])
            elif mag[j][i] == 2:
                if stack:
                    stack.clear()
                    answer += 1
        stack.clear()
                    
    print('#{}'.format(tc), answer)