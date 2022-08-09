
def star(N):
    if N == 1:
        return '*'
    else:
        print(star(N//3)*3)
        print(star(N//3) + ' '*(N//3) + star(N//3))
        print(star(N//3)*3)

N = int(input())

star(N)


# 매핑 문제에서는  중첩 리스트 중요!