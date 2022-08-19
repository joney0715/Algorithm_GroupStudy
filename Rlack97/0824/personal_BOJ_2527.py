answer = []
for i in range(4):
    boxes = list(map(int,input().split()))
    if boxes[0] < boxes[4]:
        ax1, ay1, ax2, ay2 = boxes[0],boxes[1],boxes[2],boxes[3]
        bx1, by1, bx2, by2,= boxes[4],boxes[5],boxes[6],boxes[7]
    else:
        ax1, ay1, ax2, ay2 = boxes[4],boxes[5],boxes[6],boxes[7]
        bx1, by1, bx2, by2,= boxes[0],boxes[1],boxes[2],boxes[3]

    # 박스 위치관계 정렬.
    # 따라서 ax1은 항상 bx1보다 크다.

    if by1>ay2 or bx1 > ax2 or ay1 > by2:
        answer.append('d')

        # 박스 b의 시작점이 박스 a의 종료점보다 더 밖에 있음

    elif ay2 == by1 or ax2 == bx1 or ay1 == by2:

        #  ax1 < bx1보다 크다. 이므로 박스 a의 아래, 오른쪽, 위쪽 변과 맞닿을 때

        if ax2 == bx1 and (ay2 == by1 or ay1 == by2):
            answer.append('c')
            # 오른쪽 변과 위 아래 중 하나가 맞닿으면 점

        elif bx1 < ax2 or (ay2 != by1 and ay1 != by2):
            answer.append('b')
            # 위아래 변이 일치하지 않음 == 오른쪽 변과 선
            # b의 시작점이 a의 끝점보다 앞 == 위 아래 변과 선

    else:
        answer.append('a')
        # 나머지 

for i in range(4):
    print(answer[i])