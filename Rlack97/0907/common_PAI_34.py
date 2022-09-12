# 순열 풀이
# 2022-09-04

# 1번 풀이


result = []
prev_elements = []

def DFS(elements):
    if elements == []:
        #4. 리스트 내의 모든 값을 제거해서 그래프의 끝에 도달했을 경우

        result.append(prev_elements[:]) 
        #5. 직전의 prev_element에 저장되어 있는 게 리스트 내 값으로 만든 순열이므로 
        #result 리스트에 저장

    for e in elements:
        next_elements = elements[:]
        #1. 값 변경을 방지하기 위한 복사
        next_elements.remove(e)

        prev_elements.append(e)
        #2. 자기 자신을 제외하고 prev에 추가함

        DFS(next_elements)
        #3. 남아있는 요소들로 반복하면, prev에 순열이 생성

        prev_elements.pop()
        #6. 순열 하나가 완성되면, 방문하지 않은 가지로 가기 위해 pop으로
        #prev_elements()에서 가장 최신 값을 제거
    
DFS([1,2,3])

print(result)

# 2번 풀이
import itertools

nums = [1,2,3]

print(list(itertools.permutations(nums)))
# 리스트 내 요소들이 튜플로 반환됨
print(list(map(list,itertools.permutations(nums))))
# 내부도 리스트 형태로 출력하고 싶을 경우

# itertools 모듈, 순회하면서 반복자를 생성하는데 최적화.
# 구현의 효율성과 성능을 위해, 만들어져 있는 걸 사용 안할 이유가 없다. 
# 제약이 없다면 적극 활용하자
