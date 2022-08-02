N = int(input())
shape = []
temp = 0
sumdata = 0
for i in range(N):
    shape.append(list(map(int, input().split())))
shape.sort(key = lambda x:x[0])
'''
먼저, 입력을 (위치 높이) 처럼 받게 되는데, 이를 [위치, 높이]의 리스트로 집어넣는다.
위치가 뒤죽박죽이면 알고리즘을 구현하기 복잡할 것 같아서
위치 순으로 정렬해주는 알고리즘을 짰다.
'''
if N == 1 :
    print(shape[0][1])
    quit()
'''
이 부분은 에러가 나 급하게 구현하였다. 창고 다각형이 여러 곳에 걸쳐있지 않고 막대 단 한개일 경우,
인덱스에러가 계속 나서 어쩔 수 없이 N이 1인 경우 막대의 길이만큼 출력하고 강제종료하는 부분을 만들었다.
'''
    

currentmax = shape[1][1]
for j in range(N):
    if temp < shape[j][1]:
        temp = shape[j][1]
        maxindex = j

'''
가장 큰 것을 찾는 부분. 가장 큰 것을 기준으로 좌우를 따로 계산해준다.
예를 들어 

30050007006002 이런식으로 되어있으면(1 위치에 3짜리 블럭이 있고, 4 위치에 5짜리 블럭이 있고..)
______________
3*3 + 5*4 + 7(제일 큰 부분, curmax)+ 6*3 + 2*3
이렇게 구하는 알고리즘이다.
왼쪽에서 시작, 최고점에 도달하기 전까지:
자기보다 큰 값이 나오기 계속 "curmax"만큼 더해준다
curmax: 바깥쪽에서 중앙으로 가는 과정에서 그 시점에서 마주친 가장 긴 막대의 길이(currentmax라는 뜻)
제일 큰 부분은 딱 한 블럭치만 더하기때문에 좌+우를 계산한 후 따로 더해준다.
'''

curmax = shape[0][1] #왼쪽부터 시작
for i in range(0,maxindex):
    if curmax < shape [i][1]: #현재 맥스값보다 큰게 나오면 curmax를 바꿔줌.
        curmax = shape [i][1] 
    sumdata += curmax * (shape[i+1][0]-shape[i][0])

curmax = shape[N-1][1] #오른쪽을 더해주는 부분
for i in range(N-1,maxindex,-1):
    if curmax < shape [i][1]:
        curmax = shape [i][1]
    sumdata += curmax * (shape[i][0]-shape[i-1][0])
    
sumdata += shape[maxindex][1] #가장 큰 부분을 따로 더해주는 부분
print(sumdata)

'''
코드가 매우 지저분한 점이 아쉽다.
그림을 그려서 설명해야 할 듯.... 
'''