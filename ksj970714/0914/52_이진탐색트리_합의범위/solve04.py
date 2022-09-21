from collections import deque

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
            dq, my_sum = [root], 0
            deque(dq)

            while dq:
                node = dq.popleft()
                if node:  # 위 세 줄이 스택을 쓸 때 좋은 문법이라고 생각함
                    if node.val > L:  # 노드 밸류가 L보다 크면,
                        # 왼쪽 노드가 조건에 맞을 수 있으니 더해줌.
                        dq.append(node.left)
                    if node.val < R:  # 만약 노드 밸류가 R보다 작으면,
                        # 오른쪽 노드 또한 조건에 맞을 수 있으니 더해줌.
                        dq.append(node.right)
                    if L <= node.val <= R:
                        my_sum += node.val  # 조건에 맞으면 더해줌.
        return my_sum
#왜 DFS BFS인지 탐색 순서로 설명할 것.