# 이진 트리 반전 풀이
# 2022-09-12

import collections

# 직접 풀이

root = list(map(int,input().split()))
# 리스트 형태로 입력됨
queue = collections.deque(root)
# pop(0) 지양을 위한 덱 사용

a = 1
answer = []
answer.append(queue.popleft())
# 루트노드 저장

while queue:
    T = []
        # depths 별 원소를 담기위한 리스트

    for i in range(2**a):
        T.append(queue.popleft())
        # 빈 값도 Null로 입력받으므로 원소 갯수를 기준으로 자르면 depths를 구분할 수 있음

    for i in range(len(T)-1,-1,-1):
        answer.append(T[i])
        # 분리한 해당 depths의 원소들을 역순으로 삽입

    a += 1
        # 다음 깊이로 이동

print(*answer)
    
        

# 교재 풀이 1. 재귀
def invertTree(self, root) :
    if root:
        root.left, root.right = \
            self.invertTree(root.right), self.invertTree(root.left)
        return root
# ???????
# .left나 .right는 메서드인건가?
# 재귀형태인건 어떻게든 알겠고...
# = \ 는 또 뭘까...

# 교재 풀이 2. BFS (비재귀)
def invertTree(self, root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root


# 교재 풀이 3. DFS (비재귀)

# 위와 완전히 동일한 코드이지만, 하나가 변경
def invertTree(self, root):
    stack = collections.deque([root])
    # 어차피 데크는 다 대응하므로, 굳이 이름을 바꿀 필요는 없음

    while stack:
        node = stack.pop()
        # 처음 값을 뽑은 BFS와 달리 마지막 값 추출
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

    return root

# 교재 풀이 4. DFS (비재귀-후위)
def invertTree(self, root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:      
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left

    return root

    # 후위 순회 = 왼쪽 서브트리 호출, 오른쪽 서브트리 호출 후 자기 자신을 가장 마지막으로 출력.
    # 맨 왼쪽 아래에서부터 순회하며, depths가 가장 깊은 곳부터 확인한다.
    # 근데 스택에 더하는거랑 교환하는 순서를 바뀐다고 왜 전위순회가 후위순회가 되는지는 모르겠다.