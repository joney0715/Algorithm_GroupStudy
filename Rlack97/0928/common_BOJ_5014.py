# 5014_스타트링크  풀이
# 2022-09-25
import sys
from collections import deque

F,S,G,U,D = map(int,input().split())

# S -> 위로 U층, 아래로 D층, G층으로 가야 하며 최고층이 F층


def BFS(S):
    visited[S] == 1
    q = deque([S])

    while q:
        v = q.popleft()
        if v == G:
            return count[G]
        
        for i in (v + U, v - D):
            if 0< i <=F and not visited[i]:
                visited[i] == 1
                count[i] = count[v] +1
                q.append(i)
    if count[G] == 0:
        return 'use the staris'



    return 


answer = 0
visited = [0]*(F+1)
count = [0]*(F+1)
answer = BFS(S)

print(answer)

# 재귀형태로 풀었다만, 메모리 초과 및 RecursionError로 애먹었다.
# BFS 형태에 더 익숙해질 필요가 있음.