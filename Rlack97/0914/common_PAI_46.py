# 두 이진 트리 병합  풀이
# 2022-09-12

# Treenode라는 형태의 함수를 리트코드에서 제공해주는 전제.

def add_Trees(self, t1 : TreeNode, t2 : TreeNode):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        # 새로운 트리의 해당 노드는 입력받은 두 트리의 노드의 합

        node.left = self.add_Trees(t1.left,t2.left)
        # 새로운 노드의 왼쪽 자식 노드는 입력받은 두 트리의 왼쪽 자식 노드 두개를 재귀한 값

        node.right = self.add_Trees(t1.right,t2.right)
        # 오른쪽 역시 마찬가지

        return node
        # 자기 아래쪽을 전부 호출했으면 자신을 반환

    else: 
        return t1 or t2
        # 값이 존재하는 쪽을 출력