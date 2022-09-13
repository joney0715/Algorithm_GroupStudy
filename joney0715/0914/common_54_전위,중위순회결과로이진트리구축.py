from collections import defaultdict

def buildTree(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))

        if len(inorder) == 1:
            return inorder[idx]

        left = buildTree(preorder, inorder[0:idx])
        right = buildTree(preorder, inorder[idx+1:])
        tree[inorder[idx]].append(left)
        tree[inorder[idx]].append(right)

        return inorder[idx]

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

tree = defaultdict(list)
buildTree(preorder, inorder)
print(tree)