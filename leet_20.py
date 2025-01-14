class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root):
    res =[]

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)
    inorder(root)
    return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Perform in-order traversal
print(inorder_traversal(root))