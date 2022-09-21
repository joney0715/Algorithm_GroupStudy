class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        return (root.val if L <= root.val <= R else 0) + \
               self.rangeSumBST(root.left, L, R) + \
               self.rangeSumBST(root.right, L, R)
    '''
    +/ 는 줄바꿈이 되어도 더할 수 있게 하는 일종의 문법
    left, right는 해당 노드의 왼쪽, 오른쪽을 호출하는,
    TreeNode 클래스에 대해 내부적으로 정의된 메서드라고 생각하면 된다.
    왼쪽, 오른쪽 메서드를 각각 호출해 실시.
    '''