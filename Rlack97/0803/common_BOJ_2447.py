
def star(N):
    if N == 1:
        return '*'
    else:
        print(star(N//3)*3)
        print(star(N//3) + ' '*(N//3) + star(N//3))
        print(star(N//3)*3)

N = int(input())

star(N)