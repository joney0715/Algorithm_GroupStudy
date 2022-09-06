#일정 그래프 반복 풀이법
import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b) #그래프에 추가

        #DFS 실시(우리가 흔히 아는 그 DFS)
        stack = ['JFK']
        route = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
                '''
                stack[-1]이 그래프에 존재하면 계속 stack에 append 하는 작업이 계속, 
                만약 길이 존재하면 계속 집어넣는다.(graph의 경로가 없을 때까지)
                예를 들면, 스택에 [1]이 있고,
                1 -> [2,3], 3-> [2] 인 경우, 스택에 [1,2]가 담기게 된다.
                
                다음 루프에서, 스택에 원소가 존재하므로, 2에서 다음 방향으로 향하는 경로가 들어가게 된다.
                그러나 만약, 2가 막다른 길이라면, 애초에 루프가 시작되지 않음
                (graph[stack[-1]]이 없으므로)
                이렇게 되면 해당 루프가 끝나게 된다.            
                
                '''
            route.append(stack.pop())
            '''
            위 루프가 끝나고 나면, 스택의 마지막 원소를 빼서 루트에 집어넣음
            (막다른 길)을 마지막으로 빼버림. 여행 일정 구성이기 때문에 막다른 길은 하나만 있다는 아이디어
            
            
            이후에 위의 루프에선 1 -> [3] 으로 탐색하게 된다.
            그럼 스택에 [1,3]이 담기게 되고, route에 2,3,1 순으로 담기게 되어 역순 출력하면 된다.
            '''

        print(route[::-1])






