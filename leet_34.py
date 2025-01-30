

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

    def inorder_traversal(self):
        
        if self.left:    
            self.left.inorder_traversal()
        print(self.val)
        if self.right:
            self.right.inorder_traversal()




q = TreeNode(1)
q.left = TreeNode(5)
q.right = TreeNode(7)
q.left.left = TreeNode(2)
q.left.right= TreeNode()

q.inorder_traversal()
