import heapq

t = int(input())

for i in range(t):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * k


    for j in range(k):
        com, num = input().split

        if com == 'I':
            heapq.heappush(q1, (int(num),j))
            heapq.heappush(q2, (-int(num),j))
            visited[j] = True
        
        else:
            if num == 1:
                while q2 and not visited[q2[0][1]]:
                    heapq.heappush(q2)
            else: