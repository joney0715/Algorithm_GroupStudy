import collections
import sys
sys.setrecursionlimit(5002)

N = int(input())
way = collections.defaultdict(list)

# 전제: N-1개의 선으로 이어져 있음: 순환이 없음, 즉 트리구조
# ex, 1,2,3을 순환이 있는 그래프로 만들기 위해서는 3개의 선이 필요함.. 하지만 2개만 주어짐
# 트리가 될 수밖에 없음을 생각하고 풀면, 트리 탐색으로 풀어낼 수 있음.


for i in range(N-1):
    a, b, c = map(int,input().split())
    if a > b:
        a,b = b,a
    way[a].append([b, c])
    way[b].append([a, c])
visited = [0]*(N+1)
visited[1] = 1

global hap
hap = 0
ans = [0]
def bfs(n):
    global hap
    if n != 1 and len(way[n]) == 1:
        ans.append(hap)

    for i in range(len(way[n])):
        temp = way[n][i]
        if visited[temp[0]] == 0:
            visited[temp[0]] = 1
            hap += temp[1]
            bfs(temp[0])
            hap -= temp[1]
            visited[temp[0]] = 0


bfs(1)
print(ans)
print(max(ans))