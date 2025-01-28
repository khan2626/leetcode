

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if not self.val:
            return 0
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
        
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.val)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.val)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.val)

    def find_val(self, val):
        if val < self.val:
            if not self.left:
                return False
            else:
                return self.left.find_val(val)
        elif val > self.val:
            if not self.right:
                return False
            else:
                return self.right.find_val(val)
        else:
            return True
tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(2)
tree.insert(1)
tree.insert(11)
tree.insert(22)
tree.insert(15)

tree.inorder_traversal()
print()
tree.preorder_traversal()
print()
tree.postorder_traversal()
print(tree.find_val(5))
print(tree.find_val(7))