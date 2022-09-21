class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0  # node에 대해서만 계산하게 만드는 것
            '''
            이진트리의 특성 이용, 왼쪽은 작고 오른쪽은 더 크다
            따라서 부모 노드가 L보다 작으면 더하지 않고 오른쪽만 탐색
            만약 부모 노드가 R보다 작으면 더하지 않고 왼쪽만 탐색
            '''
            if node.val < L:
                return dfs(node.right)
            if node.val > R:
                return dfs(node.left)
        #이 두 조건을 만족하지 않을 경우에 L<node.val<R이므로
            return node.val + dfs(node.left) + dfs(node.right)
        #계속 return return..하며 조건에 맞는 값일 경우 더해줌
        return dfs(root)

