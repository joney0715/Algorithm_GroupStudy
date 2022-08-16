import sys
N, K = map(int,input().split())

data = []
for i in range(N):
    data.append(int(sys.stdin.readline()))

interval=[]

for i in range(N-1):
    interval.append(data[i+1]-data[i]-1)

interval.sort()

offtime = 0

for j in range(K-1):
    offtime += interval.pop()

print(data[-1]-data[0]+1-offtime)