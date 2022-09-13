
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node):
    global value

    if node is None:
        return 0

    left = dfs(node.left)
    right = dfs(node.right)

    if node.left and node.left.val == node.val:
        left += 1
    else:
        left = 0

    if node.right and node.right.val == node.val:
        right += 1
    else:
        right = 0    

    value = max(value, left+right)

    return max(left, right)


tree = TreeNode(
    5, 
    TreeNode(4,TreeNode(1),TreeNode(1)), 
    TreeNode(5, TreeNode(), TreeNode(5))
)

value = 0
dfs(tree)
print(value)