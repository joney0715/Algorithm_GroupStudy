# 교재 풀이

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(node):
    # 직경
    global max_value
    
    # 리프 노드인 경우
    if not node:
        return -1
    
    # 왼쪽 노드, 오른쪽 노드
    left = dfs(node.left)
    right = dfs(node.right)
    print(node.val, left, right)
    # 왼쪽 노드와의 거리와 오른쪽 노드와의 거리의 합과 비교
    max_value = max(max_value, left+right+2)

    # 연결된 노드중 큰 값에 하나를 더해서 반환
    return max(left, right) + 1

# 입력값
tree = TreeNode(
    1, 
    TreeNode(2,TreeNode(4),TreeNode(5)), 
    TreeNode(3, None, None)
)

max_value = 0
dfs(tree)
print(max_value)