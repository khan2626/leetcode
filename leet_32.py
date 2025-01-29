

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if val < self.val:
            if not self.left:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            if not self.right:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

    def maxDepth(self, node):
        if not node:
            return 0
        len_left = self.left.maxDepth(node) if self.left else 0
        len_right = self.right.maxDepth(node) if self.right else 0
        return max(len_right, len_left) + 1
    



root = TreeNode(9)
root.insert(3)
root.insert(20)
root.insert(15)
root.insert(7)

# Test the maxDepth method
solution = root
depth = solution.maxDepth(root)
print(f"The maximum depth of the binary tree is: {depth}")