import collections
import sys
sys.setrecursionlimit(5002)

N = int(input())
way = collections.defaultdict(list)

for i in range(N-1):
    a, b, c = map(int,input().split())
    if a > b:
        a,b = b,a
    way[a].append([b,c])

global hap
hap = 0
ans = []
def bfs(n):
    global hap
    if way[n] == []:
        ans.append(hap)
        return

    while way[n]:
        temp = way[n].pop()
        hap += temp[1]
        bfs(temp[0])
        hap -= temp[1]

bfs(1)
print(max(ans))