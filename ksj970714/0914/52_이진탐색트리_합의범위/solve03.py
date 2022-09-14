#스택 사용한 DFS
#개인적으로, 가장 직관적이고 쉬운 풀이법이라고 생각함. 개인적으로도 제일 좋아하는 방법이예요
#이진 탐색 트리의 특성을 이용, 왼쪽은 노드보다 작고 오른쪽은 노드보다 크다. 계속 생각하며 품
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack, my_sum = [root], 0

        while stack:
            node = stack.pop()
            if node: #위 세 줄이 스택을 쓸 때 좋은 문법이라고 생각함
                if node.val > L : #노드 밸류가 L보다 크면,
                    #왼쪽 노드가 조건에 맞을 수 있으니 더해줌.
                    stack.append(node.left)
                if node.val < R : #만약 노드 밸류가 R보다 작으면,
                    #오른쪽 노드 또한 조건에 맞을 수 있으니 더해줌.
                    stack.append(node.right):
                if L <= node.val <= R:
                    my_sum += node.val #조건에 맞으면 더해줌.

        return my_sum