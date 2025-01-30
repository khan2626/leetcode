"""
it returns a boolean if binary tree "p" and "q" are same or not
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right


    def isSame(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return (self.isSame(p.left, q.left) and self.isSame(p.right, q.right))
    
p = TreeNode(1)
p.left = TreeNode(5)
p.right = TreeNode(7)
p.left.left = TreeNode(2)

q = TreeNode(1)
q.left = TreeNode(5)
q.right = TreeNode(7)
q.left.left = TreeNode(2)
#q.left.right= TreeNode()

tree = TreeNode()
solution = tree.isSame(p, q)
print(solution)