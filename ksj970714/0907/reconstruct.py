
tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
import collections

graph = collections.defaultdict(list) #keyerror 대신 디폴트 값 반환하는 딕셔너리
tickets.sort()
print(tickets)
for a,b in sorted(tickets):
    '''
    한번 정렬. 정렬 기준: 첫 원소-> 둘째 원소 순으로 자동으로 해줌.
    따라서 이렇게 정렬하고 하면 자동으로 사전 순서로 정렬됨, 
    정렬.py가 예시. 그래서 sorted 함수 한번만 사용해 원하는 순서대로 딕셔너리 만들 수 있음
    딕셔너리로 만드는 이유. 인접 리스트 방식이 간편하고 공간복잡도 면에서 더 좋음
    인접 행렬 방식을 쓰면 공간복잡도가 너무 커져, 통계학 등에서나 사용됨
    '''
    graph[a].append(b)

route = [] #리스트는 mutable, 재할당이 아니라 수정은 그냥 변경 가능(글로벌 선언 필요없음)
def dfs(point):
    while graph[point]: #경로가 없을 때까지 탐색
        dfs(graph[point].pop(0))
    route.append(point) #그림 그려 표현할 것

dfs('JFK') #JFK 지점부터 시작해 인덱싱.
print(route[::-1])