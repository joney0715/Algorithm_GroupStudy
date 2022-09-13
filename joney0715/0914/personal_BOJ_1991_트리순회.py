from collections import defaultdict

class BinaryNode():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def preorder(node):
    global preorder_list
    preorder_list += node.val
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
        
def inorder(node):
    global inorder_list
    if node.left != '.':
        inorder(tree[node.left])
    inorder_list += node.val
    if node.right != '.':
        inorder(tree[node.right])
        
def postorder(node):
    global postorder_list
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    postorder_list += node.val


N = int(input())

tree = defaultdict()
for _ in range(N):
    val, left, right = input().split()
    tree[val] = BinaryNode(val, left, right)

preorder_list = ''
inorder_list = ''
postorder_list = ''

preorder(tree[list(tree)[0]])
inorder(tree[list(tree)[0]])
postorder(tree[list(tree)[0]])

print(preorder_list)
print(inorder_list)
print(postorder_list)