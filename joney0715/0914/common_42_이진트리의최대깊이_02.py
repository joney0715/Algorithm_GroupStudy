# 교재 풀이

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    queue = deque([root])
    
    depth = 0
    while queue:
        depth += 1
        
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
    
    return depth

nums = [3, 9 ,20, 'NULL', 'NULL', 15, 7]

tree = TreeNode(
    3, 
    TreeNode(9,TreeNode(),TreeNode()), 
    TreeNode(20, TreeNode(15), TreeNode(7))
)

answer = max_depth(tree)
print(answer)