import random

K = []

for i in range(9):
	a = int(input())
	K.append(a)
# 입력값 9개를 받습니다. 

while True:                    # 무한반복문
    T = random.sample(K, 7)    # 리스트에서 7개를 무작위로 뽑고
    if sum(T) == 100:          # 그 합이 100이라면
        T.sort()               # 오름차순으로 정렬하고
        for Q in T:             
            print(Q)           # 각각을 프린트
        break                  # 푼 이후의 반복을 막기 위한 break