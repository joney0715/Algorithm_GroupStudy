class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        import collections
        graph = collections.defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []  # 리스트는 mutable, 재할당이 아니라 수정은 그냥 변경 가능(글로벌 선언 필요없음)

        def dfs(point):
            while graph[point]:  # 경로가 없을 때까지 탐색
                dfs(graph[point].pop())
            route.append(point)  # 그림 그려 표현할 것

        dfs('JFK')  # JFK 지점부터 시작해 인덱싱.
        return (route[::-1])