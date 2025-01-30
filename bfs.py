
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def bfs(root):
    q = [root]
    res = []

    while q:
        level = []
        for i in range(len(q)):
            root = q.pop(0)
            level.append(root.val)
            if root.left:
                q.append(root.left)
            if root.right:
                q.append(root.right)
        res.append(level)
    return res


#iteraative method of inorder traversal
def inorder(root):
    res = []
    stack = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Test BFS function
bfs_result = bfs(root)
print("BFS:", bfs_result)  # Output should be [[1], [2, 3], [4, 5]]

# Test iterative in-order traversal function
inorder_result = inorder(root)
print("In-order:", inorder_result)  # Output should be [4, 2, 5, 1, 3]
        