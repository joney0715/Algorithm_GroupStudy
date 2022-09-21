T = int(input())
import sys

for test in range(T):
    N = int(input())
    vec = []
    for i in range(N):
        x,y = map(int,sys.stdin.readline().split())
        vec.append([x,y])

    vec.sort(key = lambda x:x[0])

    passed_man = len(vec)
    my_min = N+1
    for idx in range(len(vec)):
        if my_min > vec[idx][1]:
            my_min = vec[idx][1]
        else:
            passed_man -= 1

    print(passed_man)